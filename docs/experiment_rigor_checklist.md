# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Existing evidence reproduced | Done | `python scripts/smoke_test.py`; `python scripts/run_evidence.py`. |
| Full-scale streamed pass | Done | `results/full_scale/*.csv`, 34,880 compact per-episode rows. |
| Corrected oracle/planner audit | Done | Final runner uses set-based A*; row-only oracle issue documented in paper. |
| Multiple suites | Done | Critical faults, prediction decoupling, threshold delay, guard scope, nonstationary, stochastic, stress. |
| Strong baselines | Done | Nominal, shield-only, batch, thresholds, cost avoidance, exact CCRA, broad guards, global action, oracle. |
| Threshold ablation | Done | `paper/tables/threshold_delay_table.tex`. |
| Guard-scope ablation | Done | `paper/tables/guard_scope_table.tex`. |
| Stale-patch stress | Done | `paper/tables/retirement_table.tex`. |
| Stochastic stress | Done | `paper/tables/stochastic_table.tex`. |
| Paper-ready figures/tables | Done | `paper/figures/*.png`, `paper/tables/*.tex`. |
| VLA boxed-link visual audit | Done | Final `C:/Users/wangz/Downloads/03.pdf`; 79 link annotations, green = 68, red = 11, cyan = 0; rendered pages 1, 3, 6, 7, 8, 9, 17, and 18. |
| Final artifact cleanup | Done | Canonical `03.pdf` only; no duplicate `3.pdf`; transient `paper/main.pdf` removed. |
| Hardware validation | Missing | Explicit limitation; not claimed. |
| Learned guard formation | Missing | Explicit limitation; not claimed. |
| Claims narrowed to evidence | Done | Manuscript, final audit, readiness decision, and reviewer docs updated. |

## Rigor Decision

Adequate for the current batch's final simulation/mechanism-paper standard. Still not a real-robot validation.

2026-06-21 delivery metadata: 25 pages, 553,427 bytes, SHA256 `3EBEAABFAC96FA12774A6441F4CF1CCDB28DAE78A0F55212AC18AD3585611F8D`.
