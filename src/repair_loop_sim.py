#!/usr/bin/env python3
"""Minimal embodied world-model repair-loop simulator.

The simulator is intentionally small and deterministic. A robot moves on a
grid from start to goal. The nominal world model knows the grid boundaries but
does not know sparse one-way contact failures. A planner repeatedly exploits
those false transitions unless the model is repaired.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from heapq import heappop, heappush
from random import Random
from typing import Iterable


State = tuple[int, int]
Action = str
TransitionKey = tuple[State, Action]

ACTIONS: tuple[tuple[Action, tuple[int, int]], ...] = (
    ("R", (1, 0)),
    ("D", (0, 1)),
    ("U", (0, -1)),
    ("L", (-1, 0)),
)


@dataclass(frozen=True)
class GridRepairEnv:
    width: int
    height: int
    start: State
    goal: State
    fault_edges: frozenset[TransitionKey]
    obstacles: frozenset[State] = frozenset()

    def nominal_step(self, state: State, action: Action) -> State:
        dx, dy = dict(ACTIONS)[action]
        nxt = (state[0] + dx, state[1] + dy)
        if (
            nxt[0] < 0
            or nxt[0] >= self.width
            or nxt[1] < 0
            or nxt[1] >= self.height
            or nxt in self.obstacles
        ):
            return state
        return nxt

    def true_step(self, state: State, action: Action) -> State:
        if (state, action) in self.fault_edges:
            return state
        return self.nominal_step(state, action)

    def states(self) -> Iterable[State]:
        for y in range(self.height):
            for x in range(self.width):
                s = (x, y)
                if s not in self.obstacles:
                    yield s


def make_env(seed: int, width: int = 15, height: int = 9) -> GridRepairEnv:
    rng = Random(seed)
    mid = height // 2
    candidates = list(range(3, width - 3))
    n_faults = 1 + (seed % 3)
    xs = sorted(rng.sample(candidates, n_faults))
    faults = frozenset((((x, mid), "R") for x in xs))
    return GridRepairEnv(
        width=width,
        height=height,
        start=(0, mid),
        goal=(width - 1, mid),
        fault_edges=faults,
    )


class RepairModel:
    name = "base"

    def predict(self, env: GridRepairEnv, state: State, action: Action) -> State:
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridRepairEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
    ) -> None:
        return None


class NominalModel(RepairModel):
    name = "nominal_no_repair"


@dataclass
class ThresholdRepairModel(RepairModel):
    threshold: int = 8
    counts: dict[TransitionKey, int] = field(default_factory=dict)
    blocked: set[TransitionKey] = field(default_factory=set)
    name = "prediction_gated_repair"

    def predict(self, env: GridRepairEnv, state: State, action: Action) -> State:
        if (state, action) in self.blocked:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridRepairEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
    ) -> None:
        if predicted == observed:
            return
        key = (state, action)
        self.counts[key] = self.counts.get(key, 0) + 1
        if self.counts[key] >= self.threshold:
            self.blocked.add(key)


@dataclass
class CCRAExactModel(RepairModel):
    blocked: set[TransitionKey] = field(default_factory=set)
    name = "ccra_exact_guard"

    def predict(self, env: GridRepairEnv, state: State, action: Action) -> State:
        if (state, action) in self.blocked:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridRepairEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
    ) -> None:
        if predicted != observed:
            self.blocked.add((state, action))


@dataclass
class CCRARowGuardModel(RepairModel):
    blocked_row_actions: set[tuple[int, Action]] = field(default_factory=set)
    name = "ccra_row_guard"

    def predict(self, env: GridRepairEnv, state: State, action: Action) -> State:
        if (state[1], action) in self.blocked_row_actions:
            return state
        return env.nominal_step(state, action)

    def observe(
        self,
        env: GridRepairEnv,
        state: State,
        action: Action,
        predicted: State,
        observed: State,
    ) -> None:
        if predicted != observed:
            self.blocked_row_actions.add((state[1], action))


@dataclass
class OracleModel(RepairModel):
    name = "oracle_fault_model"

    def predict(self, env: GridRepairEnv, state: State, action: Action) -> State:
        return env.true_step(state, action)


def heuristic(a: State, b: State) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def plan(env: GridRepairEnv, model: RepairModel, start: State) -> list[Action]:
    frontier: list[tuple[int, int, State, list[Action]]] = []
    heappush(frontier, (heuristic(start, env.goal), 0, start, []))
    best_cost: dict[State, int] = {start: 0}
    tie = 0
    while frontier:
        _, cost, state, path = heappop(frontier)
        if state == env.goal:
            return path
        for action, _ in ACTIONS:
            nxt = model.predict(env, state, action)
            if nxt == state:
                continue
            new_cost = cost + 1
            if new_cost < best_cost.get(nxt, 10**9):
                best_cost[nxt] = new_cost
                tie += 1
                priority = new_cost + heuristic(nxt, env.goal)
                heappush(frontier, (priority, tie, nxt, path + [action]))
    return []


def run_episode(
    env: GridRepairEnv,
    model: RepairModel,
    step_cap: int = 120,
) -> dict[str, int | bool]:
    state = env.start
    mismatches = 0
    replans = 0
    steps = 0
    for _ in range(step_cap):
        if state == env.goal:
            return {"success": True, "steps": steps, "mismatches": mismatches, "replans": replans}
        path = plan(env, model, state)
        replans += 1
        if not path:
            return {"success": False, "steps": steps, "mismatches": mismatches, "replans": replans}
        action = path[0]
        predicted = model.predict(env, state, action)
        observed = env.true_step(state, action)
        if predicted != observed:
            mismatches += 1
        model.observe(env, state, action, predicted, observed)
        state = observed
        steps += 1
    return {"success": state == env.goal, "steps": steps, "mismatches": mismatches, "replans": replans}


def prediction_error(env: GridRepairEnv, model: RepairModel) -> float:
    total = 0
    wrong = 0
    for state in env.states():
        for action, _ in ACTIONS:
            total += 1
            if model.predict(env, state, action) != env.true_step(state, action):
                wrong += 1
    return wrong / total if total else 0.0


def strategy_factory(name: str) -> RepairModel:
    if name == "nominal_no_repair":
        return NominalModel()
    if name == "prediction_gated_repair":
        return ThresholdRepairModel(threshold=8)
    if name == "ccra_exact_guard":
        return CCRAExactModel()
    if name == "ccra_row_guard":
        return CCRARowGuardModel()
    if name == "oracle_fault_model":
        return OracleModel()
    raise ValueError(f"unknown strategy: {name}")
