# Submission Attack Log

Paper: 03_embodied_world_model_repair_loops

Hardening version: v3
Date: 2026-06-13 20:15:00 +01:00

## Attack Rounds

| Round | Attack | Action | Residual Risk |
|---:|---|---|---|
| 1 | Exact CCRA is just one-mismatch transition blocking. | Conceded and formalized with threshold-delay sweep. | Novelty must stay on planner-facing repair contract. |
| 2 | Prediction-gated threshold 8 is arbitrary. | Swept thresholds 1, 2, 4, 8, 16, 32. | Adaptive thresholds remain future work. |
| 3 | Formal lemma is trivial. | Kept as interface pin-down only. | Reviewers may still want deeper theory. |
| 4 | Evidence is toy grid. | Expanded to 34,880-row full-scale simulation pass with seven suites. | Still no real robot. |
| 5 | Prediction loss is a strawman. | Reported task success, global prediction error, control-weighted error, counterexamples, and false blocks. | Control literature often already reports task metrics. |
| 6 | Row guard over-repairs artificially. | Added guard-scope suite with precision/recall/false-block accounting. | Learned guards are not solved. |
| 7 | Online sys-ID and residual learning are close. | Kept hostile boundary and emphasized immediate planner-facing transition contract. | Richer learned baselines remain future work. |
| 8 | No stochasticity. | Added stochastic contradiction suite. | Simple Bernoulli faults only. |
| 9 | Stale patches may become unsafe. | Added nonstationary/retirement suite. | Real stale-patch validation remains future work. |
| 10 | Oracle/planner may be weak. | Rejected row-only planner and reran with corrected set-based A*. | Still finite-grid planning. |
| 11 | Reproducibility at scale. | Added summarize-only path and compact streamed CSV rows. | Full run still takes time. |
| 12 | PDF link boxes must visually match the visible VLA-v4 role model. | Added explicit hyperref boxed-link policy, rebuilt, rendered all link-bearing pages, and verified green citation/URL boxes plus red internal-reference boxes. | Visual style is verified for this artifact; future source edits must preserve the policy. |

## Stop Condition

The v3 pass completed the recoverable local scope: corrected runner, full-scale streamed experiments, stronger baselines, ablations, stress tests, paper-ready figures/tables, a 25-page final manuscript, and explicit limitations. Remaining issues require hardware, high-fidelity simulation, or learned guard formation.

The 2026-06-21 VLA highlight-hardening pass completed visual delivery scope: `C:/Users/wangz/Downloads/03.pdf` is 25 pages, 553,427 bytes, SHA256 `3EBEAABFAC96FA12774A6441F4CF1CCDB28DAE78A0F55212AC18AD3585611F8D`, with 79 role-model-style link annotations and zero malformed page-edge rectangles.
