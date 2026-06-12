# Hostile Reviewer Response

## Likely Decision

Workshop accept / main-conference reject unless expanded with learned guards, stochastic/continuous domains, or robot experiments.

## Core Responses

| Reviewer Objection | Response in v2 |
|---|---|
| Exact CCRA is just one-mismatch blocking. | Conceded. Threshold 1 matches exact CCRA in this deterministic toy. |
| Threshold 8 baseline is arbitrary. | Added threshold sweep showing thresholds induce the same number of repeated counterexamples. |
| The lemma is trivial. | Conceded. It pins down the planner-facing obligation. |
| Prediction loss is a strawman. | Narrowed claim to sparse planner-exploited errors and update target. |
| Evidence is only a grid. | Conceded and marked workshop-only. |
| Broad row guard over-repairs. | Yes; it demonstrates success/prediction-error divergence, not a deployable guard learner. |

## Claims We Should Not Make

- Do not claim a sophisticated new learning algorithm.
- Do not claim real-robot or foundation-model readiness.
- Do not claim superiority over all online system identification or residual dynamics methods.
- Do not claim stale-patch retirement, stochastic safety, or learned guard formation is solved.
