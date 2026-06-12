# Submission Attack Log

Paper: 03_embodied_world_model_repair_loops

Hardening version: v2
Date: 2026-06-12 19:42:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | Exact CCRA is just one-mismatch transition blocking. | Added threshold sweep and conceded equivalence. | High novelty pressure. |
| 2 | Prediction-gated threshold 8 is arbitrary. | Added thresholds 1, 2, 4, 8, 16. | Other adaptive thresholds untested. |
| 3 | Formal lemma is trivial. | Kept it as mechanism pin-down, not theorem depth. | Reviewers may still dislike it. |
| 4 | Evidence is toy grid. | Marked workshop-only. | No real robot or high-fidelity sim. |
| 5 | Prediction loss is a strawman. | Narrowed to sparse planner-exploited errors and update target. | Control papers often report task metrics. |
| 6 | Row guard over-repairs artificially. | Kept as provocative broad-guard failure/success case. | Needs realistic learned guards. |
| 7 | Online sys-ID and residual learning are close. | Maintained hostile boundary; no new experiment added. | Needs stronger baseline in future. |
| 8 | No stochasticity or partial observability. | Listed as limitation. | Non-recoverable locally. |
| 9 | Stale patches may become unsafe. | Listed stale-patch retirement as future work. | Not implemented. |
| 10 | Reproducibility lacks threshold artifacts. | README and paper now list threshold outputs. | Long evidence run takes several minutes. |

## Stop Condition

Stopped before 50 rounds because recoverable issues converged on the same honest boundary: paper 03 is a deterministic proxy showing planner-facing repair value, not a scalable robot world-model result. Threshold sweep, CI reporting, docs, and claim narrowing were completed.
