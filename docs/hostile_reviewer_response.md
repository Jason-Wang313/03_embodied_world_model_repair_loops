# Hostile Reviewer Response

## Likely Decision

Final under the current batch standard as a simulation/mechanism paper. A top robotics or robot-learning submission would still need hardware or high-fidelity contact simulation, learned guards, and richer continuous/stochastic evidence.

## Core Responses

| Reviewer Objection | Response in v3 |
|---|---|
| Exact CCRA is just one-mismatch blocking. | Conceded. The threshold sweep makes this explicit; the contribution is planner-facing repair obligation and evaluation target. |
| Threshold baselines are arbitrary. | Thresholds 1, 2, 4, 8, 16, and 32 are swept; embodied counterexamples scale with threshold. |
| The lemma is trivial. | Conceded. It pins down the interface guarantee, not theorem depth. |
| Prediction loss is a strawman. | The claim is narrowed to sparse planner-exploited errors; task success, prediction error, control-weighted error, and counterexamples are all reported. |
| Evidence is only a grid. | Conceded. The final paper is a mechanism simulation paper, not hardware validation. |
| Broad guards over-repair. | Measured directly with false-block rate; action/global guards fail, and row guards succeed with high over-blocking. |
| The oracle was weak. | Corrected before final: final runner uses set-based A* over known blocked transitions. |
| Stale patches become unsafe. | Nonstationary suite and retirement baselines are included; stale false-block behavior is reported. |

## Claims We Should Not Make

- Do not claim a sophisticated new learning algorithm.
- Do not claim real-robot or foundation-model readiness.
- Do not claim superiority over all online system identification or residual dynamics methods.
- Do not claim learned guard formation is solved.
- Do not claim general stochastic safety.
