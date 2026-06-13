# Final Audit

## 1. Chosen thesis

Embodied world models should sometimes be updated by planner-facing repair loops induced by execution counterexamples, not by optimizing average next-state prediction quality alone. The concrete thesis is that sparse physical contradictions can be nearly invisible to global prediction loss while dominating robot planning, so a world model needs an immediate mechanism for repairing the transition contract used by the planner.

## 2. Broken assumption

The broken assumption is that the world-model update that matters for robot control can be obtained by improving average future prediction or globally adapting the dynamics model. The final v3 evidence shows that low global prediction error can coexist with repeated planner exploitation, and that broader repair can improve task success while worsening prediction error.

## 3. Central mechanism

Counterexample-Conditioned Repair Automata (CCRA): a nominal action/world model wrapped by an ordered set of guarded transition patches. When execution contradicts a modeled state-action outcome, the robot installs or strengthens a scoped patch that future planning must roll out instead of the old transition.

The final manuscript is explicit that deterministic exact CCRA is equivalent to one-mismatch transition blocking under exact guards. The contribution is the planner-facing repair contract, scope accounting, and evaluation target, not a complicated learning algorithm.

## 4. Strongest v3 evidence

- Full-scale runner: `python scripts/run_full_scale_repair_loops.py --seed-scale 20`
- Fast regeneration: `python scripts/run_full_scale_repair_loops.py --summarize-only`
- Corrected full-scale pass: 34,880 streamed per-episode rows across seven suites.
- Corrected planner: set-based A* over known blocked transitions; the earlier row-only oracle issue was rejected and fixed before final reporting.
- Planner-exploitation stress: nominal and shield-only have 0.00 success, low prediction error 0.003, and 252.3 first-episode counterexamples.
- Exact CCRA: 1.00 success with 1.0 first-episode counterexample in the stress suite.
- Threshold-8: 1.00 success but 8.0 first-episode counterexamples.
- Row guard: 1.00 success but false-block rate 0.87 and control-weighted error 0.264.
- Guard-scope suite: exact/local/row guards can solve, while action/global repair fail from over-blocking.
- Nonstationary suite: exact CCRA succeeds but has stale false-block rate 0.37; TTL/oracle retirement reduce stale blocks.

## 5. Literature boundary

The paper does not claim novelty for learned dynamics, MPC, visual foresight, online system identification, residual dynamics, shielding, active learning, model reconciliation, Dyna-style learning/planning integration, or foundation-model planning. The novelty boundary is the immediate planner-facing transition-contract repair induced by embodied counterexamples and evaluated by repeated-exploit prevention, repair latency, guard scope, and stale-memory behavior.

## 6. Formal claim status

The formal content is intentionally modest:

- exact deterministic no-repeat lemma;
- threshold-delay proposition;
- finite prediction-error/task-success decoupling construction.

The paper does not prove scalability, real-robot performance, learned guard quality, stochastic safety, or high-dimensional perception.

## 7. Biggest weaknesses

- No hardware validation.
- No high-fidelity contact simulation.
- Guards are hand-coded rather than learned.
- The planner is explicit A* over generated grids.
- Stochastic faults are simple Bernoulli events.
- Real tactile/contact variables are not modeled.

## 8. Paper-readiness judgment

Final under the current batch standard as a 25-page simulation/mechanism paper with a corrected full-scale evidence pass, stronger baselines, ablations, stress tests, negative controls, planner bug audit, reproducibility details, and explicit limitations.

It remains not hardware-ready. A robotics main-conference path would need real robot or high-fidelity contact evidence, learned guard formation, and richer comparisons to online adaptation and residual model learning.

## 9. Exact Downloads PDF path

`C:/Users/wangz/Downloads/03.pdf`

Final Downloads PDF verified after copy: 25 pages, 553,427 bytes.

Marker check on the Downloads PDF passed for: `Submission-hardening`, `ROBOTICS_1_60`, `Decision:`, `workshop-only`, and `Downloads`.

## 10. GitHub URL

`https://github.com/Jason-Wang313/03_embodied_world_model_repair_loops`

## 11. Final artifact rule

The local `paper/main.pdf` is a transient build artifact. After final copy and verification, remove it so the canonical final artifact is the numbered Downloads PDF.
