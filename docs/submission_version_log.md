# Submission Version Log

| Version | Date | Changes | PDF |
|---|---|---|---|
| v1 | 2026-06-11 | Generated batch paper with sparse-contact grid evidence. | `C:/Users/wangz/Downloads/03.pdf` |
| v2 | 2026-06-12 | Added threshold sweep, CI fields, threshold table, narrowed claims, and submission-readiness docs. | `C:/Users/wangz/Downloads/03.pdf` |
| v3 | 2026-06-13 | Expanded to a 25-page full-scale simulation/mechanism manuscript with corrected set-based A* planning, 34,880 streamed per-episode rows, seven stress suites, stronger baselines, guard-scope/stale-patch/stochastic ablations, generated figures/tables, and updated docs. | `C:/Users/wangz/Downloads/03.pdf` |

## v3 Evidence Delta

- `scripts/run_full_scale_repair_loops.py`: corrected full-scale streamed runner plus summarize-only mode.
- `results/full_scale/full_scale_summary.json`: 34,880 rows across seven suites.
- `results/full_scale/leaderboard.csv`: aggregate metrics by suite and baseline.
- `paper/figures/*.png`: full-scale success, prediction-success scatter, threshold delay, guard scope, stale retirement, stochastic stress.
- `paper/tables/*.tex`: leaderboard, suite rows, threshold, guard, retirement, stochastic, and baseline access tables.
- Final PDF copied to `C:/Users/wangz/Downloads/03.pdf` and verified there at 25 pages.
