#!/usr/bin/env python3
"""Synthesize literature artifacts from the Paper 03 matrix.

The CSV is the durable 1000-paper landscape artifact. This script writes the
human-facing maps used to choose the paper direction. It intentionally treats
the top-300 convention as cumulative:

    serious skim = ranks 1..300
    deep read    = ranks 1..240
    hostile set  = ranks 1..100

That matches the existing matrix labels, where the top 100 are hostile, the
next 140 are additional deep reads, and the next 60 are additional skims.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path
from textwrap import shorten


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIX = DOCS / "related_work_matrix.csv"


MECHANISM_CLUSTERS = {
    "visual foresight / video prediction": r"visual foresight|video prediction|frame prediction|action-conditioned visual",
    "learned dynamics + MPC": r"model predictive control|mpc|rollout|learned dynamics",
    "online system identification": r"system identification|parameter identification|online adaptation|online dynamics",
    "residual correction": r"residual|error model|correction",
    "sim-to-real transfer": r"sim-to-real|sim to real|domain randomization|transfer",
    "uncertainty / ensembles": r"uncertainty|ensemble|bayesian",
    "object-centric / scene graphs": r"object-centric|object centric|scene graph|relation",
    "contact / tactile dynamics": r"contact|tactile|force|friction|slip|deformable",
    "foundation / language-conditioned robotics": r"foundation|large language|language model|transformer|diffusion|value map",
    "curiosity / active exploration": r"active|curiosity|exploration|information gain",
    "movement primitives / skill models": r"movement primitive|dmp|skill|attractor",
}


HIDDEN_ASSUMPTIONS = [
    (
        "Prediction loss is a proxy for decision usefulness.",
        "Rare transition errors can dominate robot success while contributing almost nothing to average next-state loss.",
        "Optimize and repair the transition relation at planner-used counterexamples instead of optimizing global frame accuracy.",
    ),
    (
        "A world model should be globally coherent before it is trusted locally.",
        "Robots often need a local action-validity correction sooner than they need a globally better simulator.",
        "Represent repairs as guarded local patches with explicit scope and expiration.",
    ),
    (
        "Online adaptation should estimate hidden global parameters.",
        "Many failures are sparse local contact changes, object-specific affordance breaks, or tool-environment interactions.",
        "Treat repair as local transition editing, not just parameter identification.",
    ),
    (
        "Residual dynamics are smooth and additive.",
        "Contact mode changes, sticking, jamming, toppling, and occlusion break smooth residual assumptions.",
        "Use discrete repair clauses that can override the nominal transition for guarded contexts.",
    ),
    (
        "Uncertainty is calibrated enough to route intervention.",
        "Robots can be confidently wrong in familiar-looking but physically changed states.",
        "Trigger repair from execution counterexamples and planner dependency, not only model confidence.",
    ),
    (
        "Domain randomization covers deployment mismatches.",
        "The important mismatch may be a newly introduced object, worn surface, damaged gripper, or changed contact patch.",
        "Make mismatch discovery and repair part of deployment-time control.",
    ),
    (
        "The right repair signal is reward.",
        "A failed contact observation can identify a transition error before enough reward feedback accumulates.",
        "Repair from state-action-outcome contradictions in the world model.",
    ),
    (
        "A verifier can be a detached checker.",
        "If verification does not rewrite what the planner will roll out next, the same exploit can recur.",
        "Make repair a first-class update to the model used by planning.",
    ),
    (
        "Planning errors are downstream of model errors.",
        "Planners actively search for model errors because optimistic false transitions look like shortcuts.",
        "Use planner-exploitation counterexamples as the main sampling distribution.",
    ),
    (
        "Object identity and contact mode are stable through interaction.",
        "Manipulation can create new modes: wedged, stuck, slipping, occluded, saturated, or coupled.",
        "Allow repair guards to bind to sensed interaction modes rather than fixed object labels.",
    ),
    (
        "Latent states preserve the variables needed for repair.",
        "A latent can predict pixels while discarding the causal variable that explains failure.",
        "Store repair conditions in interpretable state-action predicates when available.",
    ),
    (
        "One-step accuracy determines long-horizon utility.",
        "A low one-step error can still create an impossible high-value trajectory under search.",
        "Evaluate by plan invalidation and recovery under execution.",
    ),
    (
        "The environment is stationary during deployment.",
        "Robots alter the world while acting; repairs may become stale after the object moves or the surface changes.",
        "Give repairs scope, support counts, and retirement tests.",
    ),
    (
        "Failure means insufficient data.",
        "A failure may reveal a structural omission: an action precondition missing from the model.",
        "Record failed affordances as negative transition support, not just more data.",
    ),
    (
        "Better perception solves model repair.",
        "Even perfect perception does not say which transition relation the planner should stop using.",
        "Attach repair directly to action-conditioned state changes.",
    ),
    (
        "Repair can wait for batch retraining.",
        "Embodied agents need the next plan to avoid the just-observed failure.",
        "Use immediate patch insertion followed by optional later consolidation.",
    ),
    (
        "A single model objective should serve prediction, control, and explanation.",
        "Control needs asymmetric treatment of false positives and false negatives under the planner's cost.",
        "Use a control-weighted repair objective.",
    ),
    (
        "Failure cases are independent samples.",
        "A planner can revisit the same false affordance repeatedly unless the model is changed.",
        "Guarantee no exact repeated exploitation in deterministic finite settings after exact repair.",
    ),
    (
        "Robotic world models should mainly hallucinate futures.",
        "For physical agents, the critical operation is maintaining an actionable transition contract.",
        "Center the paper on maintaining plan-valid transition contracts.",
    ),
    (
        "Language/foundation priors give enough physical common sense.",
        "Semantic plausibility can disagree with the local contact physics the robot just measured.",
        "Let grounded repair override priors in the planner-facing model.",
    ),
    (
        "Benchmark success transfers to the tail of deployment.",
        "Benchmark distributions often hide rare but repeated local mismatch modes.",
        "Stress-test sparse critical errors rather than only aggregate prediction metrics.",
    ),
    (
        "Human-designed state abstractions are fixed.",
        "The abstraction that matters may appear only after a failed interaction.",
        "Let repairs introduce new guarded distinctions inside an existing abstraction.",
    ),
    (
        "Model update magnitude should be small.",
        "A small physical change can require a discontinuous transition edit, such as 'push no longer moves this object'.",
        "Permit minimal but discontinuous edits with explicit support.",
    ),
    (
        "Recovery is a policy problem.",
        "When the same world model remains wrong, better recovery policies still plan through false transitions.",
        "Make recovery include model repair before replanning.",
    ),
]


CANDIDATE_DIRECTIONS = [
    {
        "name": "Counterexample-conditioned transition repair",
        "broken_assumption": "Prediction loss is a proxy for decision usefulness.",
        "mechanism": "Execution failures become guarded transition patches used immediately by the planner.",
        "why_strong": "Changes the central object from future generation to planner-facing repair obligations.",
        "risk": "Toy evidence may not prove scalability to high-dimensional perception.",
        "score": 9,
    },
    {
        "name": "Repair-scope calculus for stale embodied patches",
        "broken_assumption": "Deployment environments are stationary.",
        "mechanism": "Repairs carry support, invalidation tests, and retirement conditions.",
        "why_strong": "Attacks a real deployment issue but is secondary without a core repair loop.",
        "risk": "May look like cache invalidation or continual-learning hygiene.",
        "score": 7,
    },
    {
        "name": "Planner-exploitation benchmark for world models",
        "broken_assumption": "One-step accuracy determines long-horizon utility.",
        "mechanism": "Adversarially searches for state-action errors that a planner will exploit.",
        "why_strong": "Useful diagnostic but benchmark-only is forbidden unless paired with a new mechanism.",
        "risk": "Could be reviewed as new benchmark only.",
        "score": 6,
    },
    {
        "name": "Latent-to-symbol repair distillation",
        "broken_assumption": "Latents preserve repair-relevant causal variables.",
        "mechanism": "Distills failure-triggered latent differences into guard predicates.",
        "why_strong": "Could bridge foundation models and planning.",
        "risk": "Too broad for this paper without heavy perception experiments.",
        "score": 5,
    },
]


def read_rows() -> list[dict[str, str]]:
    with MATRIX.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: int(r.get("rank") or 10**9))
    return rows


def blob(row: dict[str, str]) -> str:
    return " ".join(
        [
            row.get("title", ""),
            row.get("abstract", ""),
            row.get("concepts", ""),
            row.get("actual_mechanism", ""),
            row.get("hidden_assumptions", ""),
            row.get("failure_modes_ignored", ""),
        ]
    ).lower()


def md_escape(text: str) -> str:
    return (text or "").replace("\n", " ").replace("|", "\\|").strip()


def one_line(text: str, width: int = 240) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return shorten(text, width=width, placeholder="...")


def count_clusters(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    clusters: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        text = blob(row)
        matched = False
        for name, pattern in MECHANISM_CLUSTERS.items():
            if re.search(pattern, text, flags=re.I):
                clusters[name].append(row)
                matched = True
        if not matched:
            clusters["other embodied model/control priors"].append(row)
    return dict(clusters)


def representative_titles(rows: list[dict[str, str]], n: int = 6) -> str:
    bits = []
    for row in rows[:n]:
        year = row.get("year") or "n.d."
        bits.append(f"{row.get('title', 'Untitled')} ({year})")
    return "; ".join(bits)


def write_literature_map(rows: list[dict[str, str]]) -> None:
    serious = rows[:300]
    deep = rows[:240]
    hostile = rows[:100]
    clusters = count_clusters(rows)
    serious_clusters = count_clusters(serious)
    years = Counter(r.get("year") or "unknown" for r in rows)
    venues = Counter(r.get("venue") or "unknown venue" for r in rows)

    lines = [
        "# Literature Map",
        "",
        "## Field Box",
        "Robot world models for embodied decision making: learned or hybrid action models used by robots for planning, control, manipulation, locomotion, sim-to-real transfer, tactile/contact reasoning, and foundation-model-mediated physical reasoning.",
        "",
        "The working boundary excludes purely text-only agents and purely offline vision prediction unless the model is used, or explicitly proposed for use, in robot action selection.",
        "",
        "## Coverage",
        f"- Landscape sweep: {len(rows)} entries in `docs/related_work_matrix.csv`.",
        f"- Serious skim: top {len(serious)} cumulative entries by relevance/citation heuristic.",
        f"- Deep read: top {len(deep)} cumulative entries, consisting of the 100 hostile papers plus 140 additional high-relevance papers.",
        f"- Hostile prior-work set: top {len(hostile)} entries.",
        "- Per-paper extraction fields are stored in the CSV: problem claimed, mechanism, hidden assumptions, fixed variables, ignored failures, novelty constraints, and remaining opening.",
        "",
        "## Year And Venue Shape",
        f"- Most common recent years: {', '.join(f'{y}: {c}' for y, c in years.most_common(12))}.",
        f"- Most common venues/sources: {', '.join(f'{v}: {c}' for v, c in venues.most_common(12))}.",
        "",
        "## Mechanism Clusters",
    ]

    for name, members in sorted(clusters.items(), key=lambda item: (-len(item[1]), item[0])):
        serious_n = len(serious_clusters.get(name, []))
        lines.extend(
            [
                f"### {name}",
                f"- Landscape count: {len(members)}; top-300 count: {serious_n}.",
                f"- Representative papers: {representative_titles(members)}.",
                f"- Novelty pressure: {novelty_pressure_for_cluster(name)}",
                "",
            ]
        )

    lines.extend(
        [
            "## Cross-Cutting Pattern",
            "The sweep repeatedly treats the world model as something that should become more predictive, more uncertain, more robustly pretrained, or more globally adapted. The less explored mechanism is the deployment-time loop in which a robot's failed action edits the specific transition relation that the planner will otherwise keep exploiting.",
            "",
            "## Directional Consequence",
            "A strong paper should not claim that online adaptation, residual dynamics, MPC, visual foresight, or uncertainty are new. It should instead make the planner-facing repair operation central: a failed embodied counterexample creates a scoped transition patch; future planning is obligated to respect the patch; and success is measured by preventing repeated exploitation, not by lowering average prediction loss.",
        ]
    )
    (DOCS / "literature_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def novelty_pressure_for_cluster(name: str) -> str:
    if "visual" in name:
        return "Next-frame or future-image quality is heavily occupied; novelty must be about how failures rewrite planner-facing transitions."
    if "MPC" in name or "dynamics" in name:
        return "Planning with learned dynamics is not new; the paper must change the update target and trigger distribution."
    if "system identification" in name:
        return "Online adaptation is not new; novelty requires local structural repairs beyond global parameter estimation."
    if "residual" in name:
        return "Residual correction is crowded; discontinuous guarded patches need to be central and justified."
    if "sim-to-real" in name:
        return "Training-time coverage is not enough; the contribution must operate during deployment after unexpected mismatch."
    if "uncertainty" in name:
        return "Adding uncertainty alone is weak; the repair should be triggered by embodied contradictions and planner dependency."
    if "foundation" in name:
        return "Language/foundation planning is not new; grounded repair must override semantic priors."
    if "contact" in name:
        return "Contact-aware dynamics are known; the paper must show sparse contact failures break prediction-centric evaluation."
    return "This cluster constrains broad claims; keep the central claim narrowly about repair loops."


def write_hostile(rows: list[dict[str, str]]) -> None:
    lines = [
        "# Hostile Prior Work",
        "",
        "This file lists the 100-paper hostile set from the matrix. These are the papers most likely to make a broad version of the proposed contribution sound already done. Each entry preserves the required extraction fields from `docs/related_work_matrix.csv`.",
        "",
    ]
    for row in rows[:100]:
        title = row.get("title") or "Untitled"
        rank = row.get("rank") or "?"
        year = row.get("year") or "n.d."
        lines.extend(
            [
                f"## {rank}. {title} ({year})",
                f"- Authors: {one_line(row.get('authors', ''), 260)}",
                f"- Venue: {one_line(row.get('venue', ''), 160)}",
                f"- URL/DOI: {row.get('url') or row.get('doi') or 'missing'}",
                f"- Problem claimed: {one_line(row.get('problem_claimed', ''), 360)}",
                f"- Actual mechanism introduced: {one_line(row.get('actual_mechanism', ''), 360)}",
                f"- Hidden assumptions: {one_line(row.get('hidden_assumptions', ''), 360)}",
                f"- Variables treated as fixed: {one_line(row.get('variables_treated_as_fixed', ''), 360)}",
                f"- Failure modes ignored: {one_line(row.get('failure_modes_ignored', ''), 360)}",
                f"- What it makes less novel: {one_line(row.get('what_it_makes_less_novel', ''), 360)}",
                f"- What it leaves open: {one_line(row.get('what_it_leaves_open', ''), 360)}",
                f"- Hostile reason: {one_line(row.get('hostile_reason', ''), 300)}",
                "",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: list[dict[str, str]]) -> None:
    clusters = count_clusters(rows[:300])
    lines = [
        "# Novelty Boundary Map",
        "",
        "## Not Novel Enough",
        "- A larger video/world model for robot prediction.",
        "- Lower next-frame, latent-dynamics, or reconstruction loss alone.",
        "- Standard MPC with a learned dynamics model.",
        "- Online system identification as global parameter fitting.",
        "- Residual dynamics on top of a nominal simulator.",
        "- Adding uncertainty, ensembles, active learning, or a verifier without changing the planner-facing transition relation.",
        "- LLM/foundation-model planning with existing robot skills.",
        "- A benchmark that exposes model errors without a new repair mechanism.",
        "",
        "## Crowded Mechanisms In The Top 300",
        "| Cluster | Top-300 count | Boundary imposed |",
        "| --- | ---: | --- |",
    ]
    for name, members in sorted(clusters.items(), key=lambda item: (-len(item[1]), item[0])):
        lines.append(f"| {md_escape(name)} | {len(members)} | {md_escape(novelty_pressure_for_cluster(name))} |")

    lines.extend(
        [
            "",
            "## Open Boundary",
            "The least occupied contribution shape is a control-centered repair loop: after the robot executes an action and observes a contradiction, the system creates a scoped patch to the transition relation used by the planner. The patch is not a generic confidence score, not a detached verifier, and not batch retraining. It is an immediate change to what future rollouts are allowed to assume.",
            "",
            "## Minimum Novel Claim That Survives The Hostile Set",
            "Given the surveyed prior work, the defensible claim is narrow: in sparse critical-mismatch regimes, planner-triggered local transition repair can improve embodied task success while leaving average prediction loss unimproved or even worse than a prediction-centric updater. This changes the central mechanism and metric from predictive fidelity to preventing repeated plan exploitation of false affordances.",
        ]
    )
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_decision() -> None:
    lines = [
        "# Novelty Decision",
        "",
        "## Candidate Directions",
        "| Direction | Broken assumption | Mechanism | Why it is strong | Risk | Score |",
        "| --- | --- | --- | --- | --- | ---: |",
    ]
    for c in sorted(CANDIDATE_DIRECTIONS, key=lambda x: -int(x["score"])):
        lines.append(
            "| {name} | {broken_assumption} | {mechanism} | {why_strong} | {risk} | {score} |".format(
                **{k: md_escape(str(v)) for k, v in c.items()}
            )
        )
    lines.extend(
        [
            "",
            "## Chosen Thesis",
            "Embodied world models should be evaluated and updated through repair loops induced by robot execution counterexamples, not only through next-state prediction quality. A planner-facing world model needs a mechanism for immediately installing scoped transition patches when the robot discovers that a planned action's assumed effect is false.",
            "",
            "## Chosen Mechanism",
            "Counterexample-Conditioned Repair Automata (CCRA): a nominal action model plus an ordered set of guarded transition patches. Each patch stores a state-action guard, an observed replacement outcome or forbidden affordance, support counts, and a planner-facing obligation. Planning rolls out the patched model. Execution failures add or strengthen patches. Exact repeated exploitation is eliminated in deterministic finite environments when guards are exact.",
            "",
            "## Why This Beats The Seed If Needed",
            "The seed said to make online model repair the mechanism instead of next-frame prediction quality. The literature sweep sharpens this: the repair must be planner-facing, counterexample-conditioned, and local/guarded, because online adaptation and residual learning already cover many weaker versions of repair.",
        ]
    )
    (DOCS / "novelty_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_claims() -> None:
    lines = [
        "# Claims Ledger",
        "",
        "| ID | Claim | Current support | Status |",
        "| --- | --- | --- | --- |",
        "| C1 | Average next-state prediction loss can be anti-correlated with task success when sparse transition errors lie on planner-preferred routes. | Literature motivation plus planned grid/contact experiment. | To be tested. |",
        "| C2 | A planner-facing local repair patch can prevent repeated exploitation of the exact same false transition after one observed counterexample in a deterministic finite model with exact guards. | Direct proof sketch in paper; implementation check. | Formally supportable under narrow assumptions. |",
        "| C3 | CCRA can improve success with fewer deployment failures than a prediction-centric global updater in sparse mismatch settings. | Planned simulation over randomized maps. | To be tested. |",
        "| C4 | The contribution is not online system identification because repairs can be discontinuous local transition overrides rather than global parameter estimates. | Literature boundary from hostile set. | Supported as a positioning claim. |",
        "| C5 | The contribution is not uncertainty, active learning, or verifier-only robotics because the update directly changes the model used in future planning. | Mechanism definition and ablations. | Supported if implementation includes ablations. |",
        "| C6 | The paper does not establish scalability to high-dimensional real robot perception or foundation-model robotics. | No real-robot experiment planned. | Limitation; do not overclaim. |",
        "",
        "## Formal Claim Scope",
        "The only formal claim intended for the main paper is the exact-guard no-repeat lemma: in a deterministic finite transition system, if an executed state-action pair contradicts the nominal model and the repair patch exactly matches that state-action pair, a planner using the patched model will not choose a plan whose validity depends on the old transition for that same guarded pair, unless no alternative plan exists or the planner ignores the patch. This is deliberately narrow.",
    ]
    (DOCS / "claims.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_reviewer_attacks() -> None:
    attacks = [
        (
            "This is just online system identification.",
            "No: the mechanism is a local, potentially discontinuous transition edit with guard scope. It does not assume a low-dimensional global parameter explains the mismatch. The paper should cite sys-ID as hostile and keep this distinction sharp.",
        ),
        (
            "This is just residual dynamics learning.",
            "Residual models usually optimize smooth predictive corrections. CCRA can encode a forbidden affordance or replacement transition that immediately changes planner rollouts, including discontinuities.",
        ),
        (
            "This is just MPC with a learned model.",
            "MPC is the consumer of the model, not the contribution. The contribution is the repair operation induced by planner-execution counterexamples.",
        ),
        (
            "Why not use uncertainty or ensembles?",
            "Uncertainty may help choose actions, but it does not by itself rewrite the false transition the planner will exploit. The ablation should show uncertainty-like caution is not the same as a patch.",
        ),
        (
            "The evidence is toy.",
            "True. The honest claim is mechanistic and diagnostic, not SOTA robotics performance. The paper should be positioned as a minimal mechanism paper and likely workshop/revise unless expanded with real robot or high-fidelity sim evidence.",
        ),
        (
            "The repair memory will overfit.",
            "Yes, if guards are too narrow or stale. The paper should include support counts, exact-scope claims only, and retirement/invalidation as future work unless implemented.",
        ),
        (
            "Prediction loss is a strawman because control papers evaluate task success.",
            "The attack is fair. The paper should avoid saying everyone only optimizes prediction. The narrower point is that world-model updates and benchmarks often still reward average predictive fidelity, while sparse planner-exploited errors need a different update target.",
        ),
        (
            "Active learning already collects failures.",
            "Collecting data is not enough; the core loop is immediate planner-facing transition repair before retraining.",
        ),
        (
            "Verifiers or shielding already prevent bad actions.",
            "A detached shield can block an action, but the novelty claim is updating the transition model so subsequent multi-step planning searches a different physical future.",
        ),
        (
            "The formal lemma is trivial.",
            "It is intentionally simple. Its role is to pin down the mechanism, not to be a deep theorem. The paper must lean on empirical decoupling of prediction loss and task success.",
        ),
    ]
    lines = ["# Reviewer Attacks", ""]
    for i, (attack, response) in enumerate(attacks, start=1):
        lines.extend([f"## Attack {i}: {attack}", response, ""])
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines), encoding="utf-8")


def write_assumption_table() -> None:
    lines = [
        "# Hidden Assumptions And Direction Seeds",
        "",
        "| # | Hidden assumption that may be false | Why it may fail in embodied robotics | Direction that breaks it |",
        "| ---: | --- | --- | --- |",
    ]
    for idx, (assumption, why, direction) in enumerate(HIDDEN_ASSUMPTIONS, start=1):
        lines.append(f"| {idx} | {md_escape(assumption)} | {md_escape(why)} | {md_escape(direction)} |")
    (DOCS / "hidden_assumptions.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_summary(rows: list[dict[str, str]]) -> None:
    fields_ok = all(
        all(row.get(field, "").strip() for field in ["problem_claimed", "actual_mechanism", "hidden_assumptions", "variables_treated_as_fixed", "failure_modes_ignored", "what_it_makes_less_novel", "what_it_leaves_open"])
        for row in rows[:100]
    )
    lines = [
        "# Literature Synthesis Summary",
        "",
        f"- Matrix rows: {len(rows)}.",
        "- Required CSV path: `docs/related_work_matrix.csv`.",
        "- Cumulative serious skim: ranks 1-300.",
        "- Cumulative deep read: ranks 1-240.",
        "- Hostile set: ranks 1-100.",
        f"- Hostile extraction fields complete for top 100: {'yes' if fields_ok else 'no'}.",
        "- Chosen mechanism: Counterexample-Conditioned Repair Automata (CCRA).",
        "- Chosen evaluation focus: sparse planner-exploited transition errors where prediction loss and embodied success diverge.",
    ]
    (DOCS / "literature_synthesis_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    rows = read_rows()
    if len(rows) < 1000:
        raise RuntimeError(f"Expected at least 1000 matrix rows, found {len(rows)}")
    write_literature_map(rows)
    write_hostile(rows)
    write_novelty_boundary(rows)
    write_decision()
    write_claims()
    write_reviewer_attacks()
    write_assumption_table()
    write_summary(rows)
    print(f"wrote literature synthesis from {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
