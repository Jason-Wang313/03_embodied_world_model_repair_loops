# Full-Scale Results Summary

## Final Gate

- Final manuscript target: at least 25 pages of real content.
- Verified final Downloads copy: 25 pages.
- No intermediate PDF was copied to Downloads before the final gate.

## Full-Scale Run

- Runner: `python scripts/run_full_scale_repair_loops.py --seed-scale 20`
- Fast regeneration path: `python scripts/run_full_scale_repair_loops.py --summarize-only`
- Total streamed per-episode rows: 34,880
- Raw trajectories saved: no
- Corrected planner: set-based A* over known blocked transitions.
- Claim scope: finite transition-system simulation, not hardware validation.

## Suite Rows

- `critical_sparse_faults.csv`: 9,720
- `prediction_loss_decoupling.csv`: 4,500
- `threshold_delay.csv`: 1,800
- `guard_scope.csv`: 2,100
- `nonstationary_retirement.csv`: 5,760
- `stochastic_contradictions.csv`: 5,600
- `planner_exploitation_stress.csv`: 5,400

## Headline Findings

- Planner-exploitation stress: nominal and shield-only have 0.00 success despite low prediction error 0.003.
- Exact CCRA reaches 1.00 stress success after 1.0 first-episode counterexample.
- Threshold-8 also reaches 1.00 stress success but pays 8.0 first-episode counterexamples.
- Row guards solve but over-block: stress false-block rate 0.87 and control-weighted error 0.264.
- Guard-scope suite shows action/global guards fail from overgeneralization.
- Nonstationary suite shows exact CCRA accumulates stale false blocks without retirement.
