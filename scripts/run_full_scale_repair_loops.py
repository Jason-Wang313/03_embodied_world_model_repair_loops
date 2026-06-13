#!/usr/bin/env python3
"""Full-scale streamed evidence for embodied world-model repair loops.

The original paper-03 simulator is intentionally tiny but slow to scale because
it replans by graph search at every step. This runner keeps the same mechanism
family while using a corridor planner tailored to the generated transition
systems. The goal is not a new robotics benchmark; it is a large, RAM-light
stress pass over planner-facing repair contracts.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import dataclass, field
from functools import lru_cache
from heapq import heappop, heappush
from pathlib import Path
from typing import Callable, Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGURES = RESULTS / "figures"
PAPER_FIGURES = ROOT / "paper" / "figures"
PAPER_TABLES = ROOT / "paper" / "tables"

State = tuple[int, int]
Action = str
TransitionKey = tuple[State, Action]

ACTIONS: tuple[tuple[Action, tuple[int, int]], ...] = (
    ("R", (1, 0)),
    ("D", (0, 1)),
    ("U", (0, -1)),
    ("L", (-1, 0)),
)

ACTION_DELTA = dict(ACTIONS)


@dataclass(frozen=True)
class GridEnv:
    width: int
    height: int
    start: State
    goal: State
    phase1_faults: frozenset[TransitionKey]
    offroute_faults: frozenset[TransitionKey] = frozenset()
    phase2_faults: frozenset[TransitionKey] | None = None
    switch_episode: int | None = None
    fault_probability: float = 1.0
    label: str = "env"

    def states(self) -> Iterable[State]:
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y)

    def nominal_step(self, state: State, action: Action) -> State:
        dx, dy = ACTION_DELTA[action]
        nxt = (state[0] + dx, state[1] + dy)
        if nxt[0] < 0 or nxt[0] >= self.width or nxt[1] < 0 or nxt[1] >= self.height:
            return state
        return nxt

    def active_faults(self, episode: int) -> frozenset[TransitionKey]:
        critical = self.phase1_faults
        if self.switch_episode is not None and episode >= self.switch_episode and self.phase2_faults is not None:
            critical = self.phase2_faults
        return frozenset(set(critical) | set(self.offroute_faults))

    def fault_probability_for(self, key: TransitionKey, episode: int) -> float:
        if key in self.active_faults(episode):
            return self.fault_probability
        return 0.0

    def true_step(self, state: State, action: Action, episode: int, rng: random.Random) -> State:
        key = (state, action)
        if key in self.active_faults(episode) and rng.random() < self.fault_probability:
            return state
        return self.nominal_step(state, action)

    def critical_route_keys(self) -> set[TransitionKey]:
        y = self.start[1]
        return {((x, y), "R") for x in range(self.start[0], self.goal[0])}


def sample_faults(
    rng: random.Random,
    width: int,
    height: int,
    count: int,
    row: int,
    avoid: set[int] | None = None,
) -> frozenset[TransitionKey]:
    avoid = avoid or set()
    candidates = [x for x in range(2, width - 3) if x not in avoid]
    if not candidates:
        return frozenset()
    xs = rng.sample(candidates, min(count, len(candidates)))
    return frozenset((((x, row), "R") for x in xs))


def sample_offroute_faults(
    rng: random.Random,
    width: int,
    height: int,
    count: int,
    main_row: int,
) -> frozenset[TransitionKey]:
    candidates: list[TransitionKey] = []
    for y in range(height):
        if y == main_row:
            continue
        for x in range(1, width - 2):
            candidates.append(((x, y), "R"))
    if not candidates:
        return frozenset()
    return frozenset(rng.sample(candidates, min(count, len(candidates))))


def make_env(
    seed: int,
    width: int = 25,
    height: int = 11,
    fault_count: int = 2,
    offroute_noise: int = 0,
    fault_probability: float = 1.0,
    nonstationary: str = "stable",
    switch_episode: int | None = None,
    label: str = "env",
) -> GridEnv:
    rng = random.Random(seed * 1009 + width * 37 + height * 17 + fault_count * 19 + offroute_noise)
    main_row = height // 2
    phase1 = sample_faults(rng, width, height, fault_count, main_row)
    offroute = sample_offroute_faults(rng, width, height, offroute_noise, main_row)
    phase2: frozenset[TransitionKey] | None = None
    if nonstationary == "remove":
        phase2 = frozenset()
    elif nonstationary == "move":
        avoid = {state[0] for state, _ in phase1}
        phase2 = sample_faults(rng, width, height, fault_count, main_row, avoid=avoid)
    elif nonstationary == "add":
        avoid = {state[0] for state, _ in phase1}
        phase2 = frozenset(set(phase1) | set(sample_faults(rng, width, height, fault_count, main_row, avoid=avoid)))
    return GridEnv(
        width=width,
        height=height,
        start=(0, main_row),
        goal=(width - 1, main_row),
        phase1_faults=phase1,
        offroute_faults=offroute,
        phase2_faults=phase2,
        switch_episode=switch_episode,
        fault_probability=fault_probability,
        label=label,
    )


@dataclass
class Patch:
    scope: str
    state: State
    action: Action
    created_episode: int
    support: int = 1

    def applies(self, key: TransitionKey) -> bool:
        state, action = key
        if action != self.action:
            return False
        if self.scope == "exact":
            return state == self.state
        if self.scope == "row":
            return state[1] == self.state[1]
        if self.scope == "column":
            return state[0] == self.state[0]
        if self.scope == "region1":
            return abs(state[0] - self.state[0]) <= 1 and abs(state[1] - self.state[1]) <= 1
        if self.scope == "region2":
            return abs(state[0] - self.state[0]) <= 2 and abs(state[1] - self.state[1]) <= 2
        if self.scope == "action":
            return True
        if self.scope == "all":
            return True
        raise ValueError(f"unknown patch scope {self.scope}")

    def key(self) -> tuple[object, ...]:
        return (self.scope, self.state, self.action, self.created_episode, self.support)


class RepairModel:
    name = "base"
    display = "Base"

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        return env.nominal_step(state, action)

    def edge_cost(self, env: GridEnv, state: State, action: Action, episode: int) -> float:
        return 1.0

    def shield_blocks(self, state: State, action: Action, episode: int) -> bool:
        return False

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        return None

    def end_episode(self, env: GridEnv, episode: int) -> None:
        return None

    def patch_count(self) -> int:
        return 0

    def signature(self) -> tuple[object, ...]:
        return (self.name,)


class NominalModel(RepairModel):
    name = "nominal_no_repair"
    display = "Nominal"


class OracleModel(RepairModel):
    name = "oracle_fault_model"
    display = "Oracle"

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        if env.fault_probability_for((state, action), episode) > 0.0:
            return state
        return env.nominal_step(state, action)


@dataclass
class GuardRepairModel(RepairModel):
    scope: str = "exact"
    ttl: int | None = None
    oracle_retire: bool = False
    patches: list[Patch] = field(default_factory=list)
    name: str = "ccra_exact_guard"
    display: str = "CCRA exact"

    def __post_init__(self) -> None:
        if self.name == "ccra_exact_guard" and self.scope != "exact":
            self.name = f"ccra_{self.scope}_guard"
            self.display = f"CCRA {self.scope}"

    def active_patches(self, env: GridEnv, episode: int) -> list[Patch]:
        out: list[Patch] = []
        for patch in self.patches:
            if self.ttl is not None and episode - patch.created_episode >= self.ttl:
                continue
            if self.oracle_retire and env.fault_probability_for((patch.state, patch.action), episode) == 0.0:
                continue
            out.append(patch)
        return out

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        key = (state, action)
        for patch in reversed(self.active_patches(env, episode)):
            if patch.applies(key):
                return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted == observed:
            return
        key = (state, action)
        for patch in self.patches:
            if patch.applies(key):
                patch.support += 1
                return
        self.patches.append(Patch(self.scope, state, action, episode))

    def end_episode(self, env: GridEnv, episode: int) -> None:
        self.patches = self.active_patches(env, episode + 1)

    def patch_count(self) -> int:
        return len(self.patches)

    def signature(self) -> tuple[object, ...]:
        return (self.name, tuple(p.key() for p in self.patches))


@dataclass
class ThresholdRepairModel(RepairModel):
    threshold: int = 8
    counts: dict[TransitionKey, int] = field(default_factory=dict)
    blocked: set[TransitionKey] = field(default_factory=set)
    name: str = "threshold_8"
    display: str = "Threshold 8"

    def __post_init__(self) -> None:
        self.name = f"threshold_{self.threshold}"
        self.display = f"Threshold {self.threshold}"

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        if (state, action) in self.blocked:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted == observed:
            return
        key = (state, action)
        self.counts[key] = self.counts.get(key, 0) + 1
        if self.counts[key] >= self.threshold:
            self.blocked.add(key)

    def patch_count(self) -> int:
        return len(self.blocked)

    def signature(self) -> tuple[object, ...]:
        return (self.name, tuple(sorted(self.blocked)), tuple(sorted(self.counts.items())))


@dataclass
class BatchEpisodeLearner(RepairModel):
    threshold: int = 1
    committed: set[TransitionKey] = field(default_factory=set)
    pending: dict[TransitionKey, int] = field(default_factory=dict)
    name: str = "batch_episode_retrain"
    display: str = "Batch episode"

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        if (state, action) in self.committed:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted != observed:
            key = (state, action)
            self.pending[key] = self.pending.get(key, 0) + 1

    def end_episode(self, env: GridEnv, episode: int) -> None:
        for key, count in self.pending.items():
            if count >= self.threshold:
                self.committed.add(key)
        self.pending = {}

    def patch_count(self) -> int:
        return len(self.committed)

    def signature(self) -> tuple[object, ...]:
        # Pending observations do not affect planner rollouts until end_episode.
        # Excluding them lets loop detection collapse repeated exploitation.
        return (self.name, tuple(sorted(self.committed)))


@dataclass
class CautiousCostModel(RepairModel):
    penalty: float = 12.0
    cautious: set[TransitionKey] = field(default_factory=set)
    name: str = "uncertainty_cost_avoidance"
    display: str = "Cost avoidance"

    def edge_cost(self, env: GridEnv, state: State, action: Action, episode: int) -> float:
        if (state, action) in self.cautious:
            return 1.0 + self.penalty
        return 1.0

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted != observed:
            self.cautious.add((state, action))

    def patch_count(self) -> int:
        return len(self.cautious)

    def signature(self) -> tuple[object, ...]:
        return (self.name, tuple(sorted(self.cautious)))


@dataclass
class GlobalActionModel(RepairModel):
    threshold: int = 3
    counts: dict[Action, int] = field(default_factory=dict)
    blocked_actions: set[Action] = field(default_factory=set)
    name: str = "global_action_repair"
    display: str = "Global action"

    def predict(self, env: GridEnv, state: State, action: Action, episode: int) -> State:
        if action in self.blocked_actions:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted == observed:
            return
        self.counts[action] = self.counts.get(action, 0) + 1
        if self.counts[action] >= self.threshold:
            self.blocked_actions.add(action)

    def patch_count(self) -> int:
        return len(self.blocked_actions)

    def signature(self) -> tuple[object, ...]:
        return (self.name, tuple(sorted(self.blocked_actions)), tuple(sorted(self.counts.items())))


@dataclass
class ShieldOnlyModel(RepairModel):
    shielded: set[TransitionKey] = field(default_factory=set)
    name: str = "shield_only"
    display: str = "Shield only"

    def shield_blocks(self, state: State, action: Action, episode: int) -> bool:
        return (state, action) in self.shielded

    def observe(
        self,
        env: GridEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
        episode: int,
    ) -> None:
        if predicted != observed:
            self.shielded.add((state, action))

    def patch_count(self) -> int:
        return len(self.shielded)

    def signature(self) -> tuple[object, ...]:
        return (self.name, tuple(sorted(self.shielded)))


def strategy_factory(name: str) -> RepairModel:
    if name == "nominal_no_repair":
        return NominalModel()
    if name == "oracle_fault_model":
        return OracleModel()
    if name == "ccra_exact_guard":
        return GuardRepairModel(scope="exact", name="ccra_exact_guard", display="CCRA exact")
    if name == "ccra_row_guard":
        return GuardRepairModel(scope="row", name="ccra_row_guard", display="CCRA row")
    if name == "ccra_column_guard":
        return GuardRepairModel(scope="column", name="ccra_column_guard", display="CCRA column")
    if name == "ccra_region1_guard":
        return GuardRepairModel(scope="region1", name="ccra_region1_guard", display="CCRA radius 1")
    if name == "ccra_region2_guard":
        return GuardRepairModel(scope="region2", name="ccra_region2_guard", display="CCRA radius 2")
    if name == "ccra_action_guard":
        return GuardRepairModel(scope="action", name="ccra_action_guard", display="CCRA action")
    if name == "ccra_exact_ttl2":
        return GuardRepairModel(scope="exact", ttl=2, name="ccra_exact_ttl2", display="CCRA exact TTL2")
    if name == "ccra_exact_ttl4":
        return GuardRepairModel(scope="exact", ttl=4, name="ccra_exact_ttl4", display="CCRA exact TTL4")
    if name == "ccra_exact_oracle_retire":
        return GuardRepairModel(
            scope="exact",
            oracle_retire=True,
            name="ccra_exact_oracle_retire",
            display="CCRA oracle retire",
        )
    if name.startswith("threshold_"):
        return ThresholdRepairModel(threshold=int(name.rsplit("_", 1)[1]))
    if name == "batch_episode_retrain":
        return BatchEpisodeLearner(threshold=1)
    if name == "uncertainty_cost_avoidance":
        return CautiousCostModel()
    if name == "global_action_repair":
        return GlobalActionModel()
    if name == "shield_only":
        return ShieldOnlyModel()
    raise ValueError(f"unknown strategy {name}")


def moving_keys(env: GridEnv, action: Action | None = None) -> set[TransitionKey]:
    keys: set[TransitionKey] = set()
    for state in env.states():
        for act, _ in ACTIONS:
            if action is not None and act != action:
                continue
            if env.nominal_step(state, act) != state:
                keys.add((state, act))
    return keys


def patch_keys(env: GridEnv, patch: Patch) -> set[TransitionKey]:
    keys: set[TransitionKey] = set()
    action = patch.action
    if patch.scope == "exact":
        if env.nominal_step(patch.state, action) != patch.state:
            keys.add((patch.state, action))
        return keys
    if patch.scope == "row":
        for x in range(env.width):
            state = (x, patch.state[1])
            if env.nominal_step(state, action) != state:
                keys.add((state, action))
        return keys
    if patch.scope == "column":
        for y in range(env.height):
            state = (patch.state[0], y)
            if env.nominal_step(state, action) != state:
                keys.add((state, action))
        return keys
    if patch.scope in {"region1", "region2"}:
        radius = 1 if patch.scope == "region1" else 2
        for y in range(max(0, patch.state[1] - radius), min(env.height, patch.state[1] + radius + 1)):
            for x in range(max(0, patch.state[0] - radius), min(env.width, patch.state[0] + radius + 1)):
                state = (x, y)
                if env.nominal_step(state, action) != state:
                    keys.add((state, action))
        return keys
    if patch.scope in {"action", "all"}:
        return moving_keys(env, action)
    raise ValueError(f"unknown patch scope {patch.scope}")


def all_blocked_keys(env: GridEnv, model: RepairModel, episode: int) -> set[TransitionKey]:
    if isinstance(model, GuardRepairModel):
        keys: set[TransitionKey] = set()
        for patch in model.active_patches(env, episode):
            keys.update(patch_keys(env, patch))
        return keys
    if isinstance(model, ThresholdRepairModel):
        return {key for key in model.blocked if env.nominal_step(key[0], key[1]) != key[0]}
    if isinstance(model, BatchEpisodeLearner):
        return {key for key in model.committed if env.nominal_step(key[0], key[1]) != key[0]}
    if isinstance(model, GlobalActionModel):
        keys: set[TransitionKey] = set()
        for action in model.blocked_actions:
            keys.update(moving_keys(env, action))
        return keys
    if isinstance(model, OracleModel):
        return {key for key in env.active_faults(episode) if env.nominal_step(key[0], key[1]) != key[0]}
    return set()


@lru_cache(maxsize=None)
def denominator(width: int, height: int, control_weighted: bool, start_y: int, goal_x: int) -> float:
    total = 0.0
    for y in range(height):
        for x in range(width):
            for action, (dx, dy) in ACTIONS:
                nx = x + dx
                ny = y + dy
                weight = 1.0
                if control_weighted:
                    if y == start_y and action == "R" and x < goal_x:
                        weight = 25.0
                    elif action == "R" and abs(y - start_y) <= 1:
                        weight = 5.0
                total += weight
    return total


def key_weight(env: GridEnv, key: TransitionKey, control_weighted: bool) -> float:
    if not control_weighted:
        return 1.0
    state, action = key
    if state[1] == env.start[1] and action == "R" and state[0] < env.goal[0]:
        return 25.0
    if action == "R" and abs(state[1] - env.start[1]) <= 1:
        return 5.0
    return 1.0


def prediction_error_from_blocked(
    env: GridEnv,
    blocked: set[TransitionKey],
    episode: int,
    control_weighted: bool = False,
) -> float:
    active = set(env.active_faults(episode))
    keys = blocked | active
    wrong = 0.0
    for key in keys:
        p_fault = env.fault_probability_for(key, episode)
        is_blocked = key in blocked
        if is_blocked:
            expected_error = 1.0 - p_fault
        else:
            expected_error = p_fault
        wrong += key_weight(env, key, control_weighted) * expected_error
    total_weight = denominator(env.width, env.height, control_weighted, env.start[1], env.goal[0])
    return wrong / total_weight if total_weight else 0.0


def prediction_error(env: GridEnv, model: RepairModel, episode: int, control_weighted: bool = False) -> float:
    return prediction_error_from_blocked(env, all_blocked_keys(env, model, episode), episode, control_weighted)


def guard_metrics_from_blocked(env: GridEnv, blocked: set[TransitionKey], episode: int) -> dict[str, float]:
    active = set(env.active_faults(episode))
    tp = len(blocked & active)
    fp = len(blocked - active)
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / len(active) if active else 1.0
    return {
        "blocked_key_count": float(len(blocked)),
        "guard_true_positive": float(tp),
        "guard_false_positive": float(fp),
        "guard_precision": precision,
        "guard_recall": recall,
        "false_block_rate": fp / len(blocked) if blocked else 0.0,
    }


def guard_metrics(env: GridEnv, model: RepairModel, episode: int) -> dict[str, float]:
    return guard_metrics_from_blocked(env, all_blocked_keys(env, model, episode), episode)


def candidate_rows(current_y: int, goal_y: int, height: int) -> list[int]:
    rows = list(range(height))
    rows.sort(key=lambda y: (abs(y - current_y) + abs(y - goal_y), abs(y - goal_y), y))
    return rows


def vertical_actions(from_y: int, to_y: int) -> list[Action]:
    if to_y > from_y:
        return ["D"] * (to_y - from_y)
    if to_y < from_y:
        return ["U"] * (from_y - to_y)
    return []


def rollout_prediction_path(
    env: GridEnv,
    model: RepairModel,
    start: State,
    actions: list[Action],
    episode: int,
) -> tuple[bool, float, State]:
    state = start
    cost = 0.0
    for action in actions:
        nxt = model.predict(env, state, action, episode)
        if nxt == state:
            return False, math.inf, state
        cost += model.edge_cost(env, state, action, episode)
        state = nxt
    return state == env.goal, cost, state


def plan(env: GridEnv, model: RepairModel, start: State, episode: int) -> list[Action]:
    if start == env.goal:
        return []
    blocked = all_blocked_keys(env, model, episode)
    frontier: list[tuple[float, int, float, State, list[Action]]] = []
    tie = 0
    heappush(frontier, (abs(start[0] - env.goal[0]) + abs(start[1] - env.goal[1]), tie, 0.0, start, []))
    best_cost: dict[State, float] = {start: 0.0}
    while frontier:
        _, _, cost, state, path = heappop(frontier)
        if state == env.goal:
            return path
        if cost > best_cost.get(state, math.inf):
            continue
        for action, _ in ACTIONS:
            key = (state, action)
            if key in blocked:
                continue
            nxt = env.nominal_step(state, action)
            if nxt == state:
                continue
            edge_cost = model.edge_cost(env, state, action, episode)
            new_cost = cost + edge_cost
            if new_cost < best_cost.get(nxt, math.inf):
                best_cost[nxt] = new_cost
                tie += 1
                priority = new_cost + abs(nxt[0] - env.goal[0]) + abs(nxt[1] - env.goal[1])
                heappush(frontier, (priority, tie, new_cost, nxt, path + [action]))
    return []


def run_episode(
    env: GridEnv,
    model: RepairModel,
    episode: int,
    rng: random.Random,
    step_cap: int,
) -> dict[str, object]:
    state = env.start
    mismatches = 0
    replans = 0
    steps = 0
    shield_blocks = 0
    repeated_loop = 0
    seen: set[tuple[State, tuple[object, ...]]] = set()

    while steps < step_cap:
        if state == env.goal:
            return {
                "success": True,
                "steps": steps,
                "mismatches": mismatches,
                "replans": replans,
                "shield_blocks": shield_blocks,
                "repeated_loop": repeated_loop,
            }
        sig = (state, model.signature())
        if sig in seen:
            remaining = step_cap - steps
            mismatches += remaining
            steps += remaining
            repeated_loop = 1
            return {
                "success": False,
                "steps": steps,
                "mismatches": mismatches,
                "replans": replans,
                "shield_blocks": shield_blocks,
                "repeated_loop": repeated_loop,
            }
        seen.add(sig)
        path = plan(env, model, state, episode)
        replans += 1
        if not path:
            return {
                "success": False,
                "steps": steps,
                "mismatches": mismatches,
                "replans": replans,
                "shield_blocks": shield_blocks,
                "repeated_loop": repeated_loop,
            }
        action = path[0]
        predicted = model.predict(env, state, action, episode)
        if model.shield_blocks(state, action, episode):
            observed = state
            shield_blocks += 1
        else:
            observed = env.true_step(state, action, episode, rng)
        if predicted != observed:
            mismatches += 1
        model.observe(env, state, action, predicted, observed, episode)
        state = observed
        steps += 1

    return {
        "success": state == env.goal,
        "steps": steps,
        "mismatches": mismatches,
        "replans": replans,
        "shield_blocks": shield_blocks,
        "repeated_loop": repeated_loop,
    }


def write_row(writer: csv.DictWriter, row: dict[str, object]) -> None:
    writer.writerow(row)


def run_config(
    suite: str,
    config_id: str,
    env_factory: Callable[[int], GridEnv],
    strategies: list[str],
    seed_count: int,
    episodes: int,
    step_cap: int,
    writer: csv.DictWriter,
) -> int:
    rows = 0
    for seed in range(seed_count):
        for strategy in strategies:
            env = env_factory(seed)
            model = strategy_factory(strategy)
            for episode in range(episodes):
                rng = random.Random(seed * 1000003 + episode * 9176 + sum(ord(c) for c in strategy))
                out = run_episode(env, model, episode, rng, step_cap)
                blocked = all_blocked_keys(env, model, episode)
                final_pred = prediction_error_from_blocked(env, blocked, episode)
                final_control = prediction_error_from_blocked(env, blocked, episode, control_weighted=True)
                gm = guard_metrics_from_blocked(env, blocked, episode)
                row = {
                    "suite": suite,
                    "config_id": config_id,
                    "env_label": env.label,
                    "seed": seed,
                    "strategy": strategy,
                    "display": model.display,
                    "episode": episode,
                    "width": env.width,
                    "height": env.height,
                    "fault_count": len(env.phase1_faults),
                    "active_fault_count": len(env.active_faults(episode)),
                    "offroute_fault_count": len(env.offroute_faults),
                    "fault_probability": env.fault_probability,
                    "switch_episode": "" if env.switch_episode is None else env.switch_episode,
                    "success": int(bool(out["success"])),
                    "steps": int(out["steps"]),
                    "mismatches": int(out["mismatches"]),
                    "replans": int(out["replans"]),
                    "shield_blocks": int(out["shield_blocks"]),
                    "repeated_loop": int(out["repeated_loop"]),
                    "patch_count": model.patch_count(),
                    "initial_prediction_error": "",
                    "final_prediction_error": final_pred,
                    "initial_control_weighted_error": "",
                    "final_control_weighted_error": final_control,
                    **gm,
                }
                write_row(writer, row)
                rows += 1
                model.end_episode(env, episode)
    return rows


ROW_FIELDS = [
    "suite",
    "config_id",
    "env_label",
    "seed",
    "strategy",
    "display",
    "episode",
    "width",
    "height",
    "fault_count",
    "active_fault_count",
    "offroute_fault_count",
    "fault_probability",
    "switch_episode",
    "success",
    "steps",
    "mismatches",
    "replans",
    "shield_blocks",
    "repeated_loop",
    "patch_count",
    "initial_prediction_error",
    "final_prediction_error",
    "initial_control_weighted_error",
    "final_control_weighted_error",
    "blocked_key_count",
    "guard_true_positive",
    "guard_false_positive",
    "guard_precision",
    "guard_recall",
    "false_block_rate",
]


def generate_suites(seed_scale: int) -> dict[str, int]:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    PAPER_FIGURES.mkdir(parents=True, exist_ok=True)
    PAPER_TABLES.mkdir(parents=True, exist_ok=True)
    suite_rows: dict[str, int] = {}

    main_strategies = [
        "nominal_no_repair",
        "shield_only",
        "batch_episode_retrain",
        "threshold_8",
        "uncertainty_cost_avoidance",
        "ccra_exact_guard",
        "ccra_row_guard",
        "global_action_repair",
        "oracle_fault_model",
    ]

    suites: list[tuple[str, str, list[tuple[str, Callable[[int], GridEnv]]], list[str], int, int, int]] = []

    critical_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for width in [15, 25, 35]:
        for faults in [1, 2, 4]:
            config_id = f"w{width}_f{faults}"
            critical_configs.append(
                (
                    config_id,
                    lambda seed, width=width, faults=faults: make_env(
                        seed,
                        width=width,
                        height=max(9, width // 3),
                        fault_count=faults,
                        label=config_id,
                    ),
                )
            )
    suites.append(("critical_sparse_faults", "critical_sparse_faults.csv", critical_configs, main_strategies, seed_scale, 6, 180))

    decoupling_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for noise in [0, 5, 20, 60, 120]:
        config_id = f"offroute{noise}"
        decoupling_configs.append(
            (
                config_id,
                lambda seed, noise=noise: make_env(
                    seed,
                    width=31,
                    height=15,
                    fault_count=2,
                    offroute_noise=noise,
                    label=config_id,
                ),
            )
        )
    suites.append(("prediction_loss_decoupling", "prediction_loss_decoupling.csv", decoupling_configs, main_strategies, seed_scale, 5, 180))

    threshold_strategies = [f"threshold_{value}" for value in [1, 2, 4, 8, 16, 32]]
    threshold_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for faults in [1, 3, 5]:
        config_id = f"faults{faults}"
        threshold_configs.append(
            (
                config_id,
                lambda seed, faults=faults: make_env(seed, width=31, height=13, fault_count=faults, label=config_id),
            )
        )
    suites.append(("threshold_delay", "threshold_delay.csv", threshold_configs, threshold_strategies, seed_scale, 5, 220))

    guard_strategies = [
        "ccra_exact_guard",
        "ccra_row_guard",
        "ccra_column_guard",
        "ccra_region1_guard",
        "ccra_region2_guard",
        "ccra_action_guard",
        "global_action_repair",
    ]
    guard_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for faults in [1, 3, 5]:
        config_id = f"faults{faults}"
        guard_configs.append(
            (
                config_id,
                lambda seed, faults=faults: make_env(seed, width=31, height=13, fault_count=faults, label=config_id),
            )
        )
    suites.append(("guard_scope", "guard_scope.csv", guard_configs, guard_strategies, seed_scale, 5, 220))

    retire_strategies = [
        "nominal_no_repair",
        "ccra_exact_guard",
        "ccra_exact_ttl2",
        "ccra_exact_ttl4",
        "ccra_exact_oracle_retire",
        "oracle_fault_model",
    ]
    nonstationary_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for mode in ["remove", "move", "add"]:
        for switch_episode in [2, 4]:
            config_id = f"{mode}_at{switch_episode}"
            nonstationary_configs.append(
                (
                    config_id,
                    lambda seed, mode=mode, switch_episode=switch_episode: make_env(
                        seed,
                        width=31,
                        height=13,
                        fault_count=3,
                        nonstationary=mode,
                        switch_episode=switch_episode,
                        label=config_id,
                    ),
                )
            )
    suites.append(("nonstationary_retirement", "nonstationary_retirement.csv", nonstationary_configs, retire_strategies, seed_scale, 8, 220))

    stochastic_strategies = [
        "nominal_no_repair",
        "threshold_2",
        "threshold_4",
        "threshold_8",
        "ccra_exact_guard",
        "uncertainty_cost_avoidance",
        "oracle_fault_model",
    ]
    stochastic_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for prob in [0.10, 0.25, 0.50, 0.75, 1.00]:
        config_id = f"p{prob:.2f}"
        stochastic_configs.append(
            (
                config_id,
                lambda seed, prob=prob: make_env(
                    seed,
                    width=31,
                    height=13,
                    fault_count=3,
                    fault_probability=prob,
                    label=config_id,
                ),
            )
        )
    suites.append(("stochastic_contradictions", "stochastic_contradictions.csv", stochastic_configs, stochastic_strategies, seed_scale, 8, 220))

    stress_configs: list[tuple[str, Callable[[int], GridEnv]]] = []
    for width, faults in [(21, 1), (21, 4), (35, 2), (35, 6), (45, 4), (45, 8)]:
        config_id = f"w{width}_f{faults}"
        stress_configs.append(
            (
                config_id,
                lambda seed, width=width, faults=faults: make_env(
                    seed,
                    width=width,
                    height=max(11, width // 3),
                    fault_count=faults,
                    label=config_id,
                ),
            )
        )
    suites.append(("planner_exploitation_stress", "planner_exploitation_stress.csv", stress_configs, main_strategies, seed_scale, 5, 260))

    for suite_name, filename, configs, strategies, seeds, episodes, step_cap in suites:
        path = RESULTS / filename
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=ROW_FIELDS)
            writer.writeheader()
            rows = 0
            for config_id, env_factory in configs:
                rows += run_config(suite_name, config_id, env_factory, strategies, seeds, episodes, step_cap, writer)
        suite_rows[suite_name] = rows
        print(f"{suite_name}: {rows} rows")
    return suite_rows


def load_rows() -> Iterable[dict[str, str]]:
    for path in sorted(RESULTS.glob("*.csv")):
        if path.name in {"leaderboard.csv"}:
            continue
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield row


def f(row: dict[str, str], key: str) -> float:
    value = row.get(key, "")
    if value == "":
        return 0.0
    return float(value)


def summarize() -> tuple[list[dict[str, object]], dict[str, object]]:
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    suite_counts: dict[str, int] = {}
    for row in load_rows():
        key = (row["suite"], row["strategy"], row["display"])
        groups.setdefault(key, []).append(row)
        suite_counts[row["suite"]] = suite_counts.get(row["suite"], 0) + 1

    leaderboard: list[dict[str, object]] = []
    for (suite, strategy, display), rows in sorted(groups.items()):
        first_rows = [row for row in rows if int(float(row["episode"])) == 0]
        final_rows = rows
        leaderboard.append(
            {
                "suite": suite,
                "strategy": strategy,
                "display": display,
                "rows": len(rows),
                "first_episode_success": statistics.fmean(f(row, "success") for row in first_rows) if first_rows else 0.0,
                "all_episode_success": statistics.fmean(f(row, "success") for row in rows),
                "mean_first_counterexamples": statistics.fmean(f(row, "mismatches") for row in first_rows) if first_rows else 0.0,
                "mean_counterexamples": statistics.fmean(f(row, "mismatches") for row in rows),
                "mean_steps": statistics.fmean(f(row, "steps") for row in rows),
                "mean_repeated_loop": statistics.fmean(f(row, "repeated_loop") for row in rows),
                "mean_final_prediction_error": statistics.fmean(f(row, "final_prediction_error") for row in final_rows),
                "mean_final_control_error": statistics.fmean(f(row, "final_control_weighted_error") for row in final_rows),
                "mean_patch_count": statistics.fmean(f(row, "patch_count") for row in final_rows),
                "mean_guard_precision": statistics.fmean(f(row, "guard_precision") for row in final_rows),
                "mean_guard_recall": statistics.fmean(f(row, "guard_recall") for row in final_rows),
                "mean_false_block_rate": statistics.fmean(f(row, "false_block_rate") for row in final_rows),
            }
        )

    with (RESULTS / "leaderboard.csv").open("w", encoding="utf-8", newline="") as fcsv:
        fieldnames = list(leaderboard[0].keys()) if leaderboard else []
        writer = csv.DictWriter(fcsv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leaderboard)

    summary = {
        "total_rows": sum(suite_counts.values()),
        "suite_rows": suite_counts,
        "leaderboard_rows": len(leaderboard),
    }
    (RESULTS / "full_scale_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return leaderboard, summary


def rows_for(leaderboard: list[dict[str, object]], suite: str) -> list[dict[str, object]]:
    return [row for row in leaderboard if row["suite"] == suite]


def metric(row: dict[str, object], key: str) -> float:
    return float(row[key])


def savefig(name: str) -> None:
    out = FIGURES / name
    plt.tight_layout()
    plt.savefig(out, dpi=180)
    plt.savefig(PAPER_FIGURES / name, dpi=180)
    plt.close()


def write_figures(leaderboard: list[dict[str, object]]) -> None:
    stress = sorted(rows_for(leaderboard, "planner_exploitation_stress"), key=lambda r: metric(r, "all_episode_success"))
    plt.figure(figsize=(8.2, 4.8))
    plt.barh([str(r["display"]) for r in stress], [metric(r, "all_episode_success") for r in stress], color="#3b7ea1")
    plt.xlabel("All-episode success")
    plt.xlim(0, 1.05)
    plt.title("Planner-exploitation stress success")
    savefig("full_scale_success_leaderboard.png")

    plt.figure(figsize=(6.5, 4.8))
    for suite in ["critical_sparse_faults", "prediction_loss_decoupling", "guard_scope"]:
        data = rows_for(leaderboard, suite)
        plt.scatter(
            [metric(r, "mean_final_prediction_error") for r in data],
            [metric(r, "all_episode_success") for r in data],
            s=55,
            label=suite.replace("_", " "),
            alpha=0.75,
        )
    plt.xlabel("Mean final prediction error")
    plt.ylabel("All-episode success")
    plt.ylim(-0.03, 1.05)
    plt.title("Prediction error and embodied success can decouple")
    plt.legend(fontsize=8)
    savefig("prediction_success_scatter.png")

    threshold = sorted(rows_for(leaderboard, "threshold_delay"), key=lambda r: int(str(r["strategy"]).split("_")[-1]))
    plt.figure(figsize=(6.8, 4.4))
    plt.plot(
        [int(str(r["strategy"]).split("_")[-1]) for r in threshold],
        [metric(r, "mean_first_counterexamples") for r in threshold],
        marker="o",
        color="#8b3a3a",
    )
    plt.xscale("log", base=2)
    plt.xlabel("Mismatch threshold")
    plt.ylabel("Mean first-episode counterexamples")
    plt.title("Delayed repair pays embodied counterexamples")
    savefig("threshold_delay_curve.png")

    guard = rows_for(leaderboard, "guard_scope")
    plt.figure(figsize=(6.8, 4.8))
    plt.scatter(
        [metric(r, "mean_false_block_rate") for r in guard],
        [metric(r, "all_episode_success") for r in guard],
        s=[40 + 160 * metric(r, "mean_guard_recall") for r in guard],
        color="#2a9d55",
        alpha=0.75,
    )
    for row in guard:
        plt.text(metric(row, "mean_false_block_rate") + 0.01, metric(row, "all_episode_success"), str(row["display"]), fontsize=7)
    plt.xlabel("False-block rate")
    plt.ylabel("All-episode success")
    plt.ylim(-0.03, 1.05)
    plt.title("Guard scope trades recall for over-repair")
    savefig("guard_scope_frontier.png")

    nonstat = rows_for(leaderboard, "nonstationary_retirement")
    plt.figure(figsize=(8.0, 4.8))
    labels = [str(r["display"]) for r in nonstat]
    vals = [metric(r, "all_episode_success") for r in nonstat]
    order = sorted(range(len(labels)), key=lambda i: vals[i])
    plt.barh([labels[i] for i in order], [vals[i] for i in order], color="#7b5ea7")
    plt.xlabel("All-episode success")
    plt.xlim(0, 1.05)
    plt.title("Stale-patch retirement under nonstationarity")
    savefig("stale_retirement_curve.png")

    stochastic = rows_for(leaderboard, "stochastic_contradictions")
    plt.figure(figsize=(7.2, 4.8))
    for display in sorted({str(r["display"]) for r in stochastic}):
        data = [r for r in stochastic if str(r["display"]) == display]
        # Leaderboard is aggregate over probabilities, so this figure uses raw rows.
    prob_points: dict[tuple[str, str], list[float]] = {}
    for path in [RESULTS / "stochastic_contradictions.csv"]:
        with path.open("r", encoding="utf-8", newline="") as fcsv:
            for row in csv.DictReader(fcsv):
                key = (row["display"], row["config_id"])
                prob_points.setdefault(key, []).append(float(row["success"]))
    displays = sorted({key[0] for key in prob_points})
    for display in displays:
        xs: list[float] = []
        ys: list[float] = []
        for prob_label in sorted({key[1] for key in prob_points if key[0] == display}):
            xs.append(float(prob_label[1:]))
            ys.append(statistics.fmean(prob_points[(display, prob_label)]))
        plt.plot(xs, ys, marker="o", label=display)
    plt.xlabel("Fault failure probability")
    plt.ylabel("Success")
    plt.ylim(-0.03, 1.05)
    plt.title("Stochastic contradiction stress")
    plt.legend(fontsize=7, ncol=2)
    savefig("stochastic_success_curve.png")


def tex_escape(text: object) -> str:
    return str(text).replace("_", "\\_")


def write_latex_table(path: Path, columns: list[str], rows: list[list[object]], aligns: str | None = None) -> None:
    aligns = aligns or ("l" + "r" * (len(columns) - 1))
    lines = ["% Auto-generated by scripts/run_full_scale_repair_loops.py", f"\\begin{{tabular}}{{{aligns}}}", "\\toprule"]
    lines.append(" & ".join(columns) + " \\\\")
    lines.append("\\midrule")
    for row in rows:
        lines.append(" & ".join(tex_escape(item) for item in row) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_tables(leaderboard: list[dict[str, object]], summary: dict[str, object]) -> None:
    main_order = [
        "nominal_no_repair",
        "shield_only",
        "batch_episode_retrain",
        "threshold_8",
        "uncertainty_cost_avoidance",
        "ccra_exact_guard",
        "ccra_row_guard",
        "global_action_repair",
        "oracle_fault_model",
    ]
    stress = {row["strategy"]: row for row in rows_for(leaderboard, "planner_exploitation_stress")}
    write_latex_table(
        PAPER_TABLES / "full_scale_leaderboard.tex",
        ["Method", "Success", "First CE", "Pred. err", "Ctrl err", "False block"],
        [
            [
                stress[name]["display"],
                f"{metric(stress[name], 'all_episode_success'):.2f}",
                f"{metric(stress[name], 'mean_first_counterexamples'):.1f}",
                f"{metric(stress[name], 'mean_final_prediction_error'):.3f}",
                f"{metric(stress[name], 'mean_final_control_error'):.3f}",
                f"{metric(stress[name], 'mean_false_block_rate'):.2f}",
            ]
            for name in main_order
            if name in stress
        ],
    )

    threshold = sorted(rows_for(leaderboard, "threshold_delay"), key=lambda r: int(str(r["strategy"]).split("_")[-1]))
    write_latex_table(
        PAPER_TABLES / "threshold_delay_table.tex",
        ["Threshold", "Success", "First CE", "Mean CE", "Pred. err"],
        [
            [
                str(row["strategy"]).split("_")[-1],
                f"{metric(row, 'all_episode_success'):.2f}",
                f"{metric(row, 'mean_first_counterexamples'):.1f}",
                f"{metric(row, 'mean_counterexamples'):.1f}",
                f"{metric(row, 'mean_final_prediction_error'):.3f}",
            ]
            for row in threshold
        ],
    )

    guard = sorted(rows_for(leaderboard, "guard_scope"), key=lambda r: metric(r, "mean_false_block_rate"))
    write_latex_table(
        PAPER_TABLES / "guard_scope_table.tex",
        ["Guard", "Success", "Recall", "Precision", "False block", "Pred. err"],
        [
            [
                row["display"],
                f"{metric(row, 'all_episode_success'):.2f}",
                f"{metric(row, 'mean_guard_recall'):.2f}",
                f"{metric(row, 'mean_guard_precision'):.2f}",
                f"{metric(row, 'mean_false_block_rate'):.2f}",
                f"{metric(row, 'mean_final_prediction_error'):.3f}",
            ]
            for row in guard
        ],
    )

    nonstat = sorted(rows_for(leaderboard, "nonstationary_retirement"), key=lambda r: str(r["display"]))
    write_latex_table(
        PAPER_TABLES / "retirement_table.tex",
        ["Method", "Success", "False block", "Pred. err", "Patches"],
        [
            [
                row["display"],
                f"{metric(row, 'all_episode_success'):.2f}",
                f"{metric(row, 'mean_false_block_rate'):.2f}",
                f"{metric(row, 'mean_final_prediction_error'):.3f}",
                f"{metric(row, 'mean_patch_count'):.1f}",
            ]
            for row in nonstat
        ],
    )

    stochastic = sorted(rows_for(leaderboard, "stochastic_contradictions"), key=lambda r: str(r["display"]))
    write_latex_table(
        PAPER_TABLES / "stochastic_table.tex",
        ["Method", "Success", "CE/ep", "Pred. err", "False block"],
        [
            [
                row["display"],
                f"{metric(row, 'all_episode_success'):.2f}",
                f"{metric(row, 'mean_counterexamples'):.1f}",
                f"{metric(row, 'mean_final_prediction_error'):.3f}",
                f"{metric(row, 'mean_false_block_rate'):.2f}",
            ]
            for row in stochastic
        ],
    )

    write_latex_table(
        PAPER_TABLES / "suite_row_table.tex",
        ["Suite", "Rows"],
        [[suite, count] for suite, count in sorted(dict(summary["suite_rows"]).items())],
    )

    write_latex_table(
        PAPER_TABLES / "baseline_access_table.tex",
        ["Baseline", "Planner-facing update", "Generalizes", "Retires"],
        [
            ["Nominal", "No", "No", "No"],
            ["Shield only", "No transition rewrite", "No", "No"],
            ["Batch episode", "After episode", "Exact", "No"],
            ["Threshold", "After k mismatches", "Exact", "No"],
            ["Cost avoidance", "Cost only", "Exact", "No"],
            ["CCRA exact", "Immediate transition patch", "Exact", "No"],
            ["CCRA row", "Immediate transition patch", "Row", "No"],
            ["Global action", "Immediate broad patch", "Action", "No"],
            ["Oracle", "True transition model", "True faults", "Yes"],
        ],
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summarize-only", action="store_true")
    parser.add_argument("--seed-scale", type=int, default=80, help="seeds per suite config")
    args = parser.parse_args()

    if not args.summarize_only:
        suite_rows = generate_suites(args.seed_scale)
    else:
        suite_rows = {}

    leaderboard, summary = summarize()
    if suite_rows:
        summary["generated_suite_rows"] = suite_rows
        (RESULTS / "full_scale_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    write_tables(leaderboard, summary)
    write_figures(leaderboard)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
