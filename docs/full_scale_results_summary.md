# Full-Scale Results Summary

## Final Gate

- Final manuscript target: at least 25 pages of real content.
- Verified final Downloads copy: 25 pages.
- No intermediate PDF was copied to Downloads before the final gate.
- 2026-06-21 canonical PDF after VLA boxed-link hardening: `C:/Users/wangz/Downloads/03.pdf`, 25 pages, 553,427 bytes, SHA256 `3EBEAABFAC96FA12774A6441F4CF1CCDB28DAE78A0F55212AC18AD3585611F8D`.
- Final link inventory: 79 annotations; green = 68, red = 11, cyan = 0; all borders `(0, 0, 1)`; zero malformed page-edge rectangles.

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

## Visual Delivery Check

- VLA-style boxed links are explicitly pinned in `paper/main.tex`.
- Link-bearing pages rendered and inspected: 1, 3, 6, 7, 8, 9, 17, and 18.
- Visual result matches the visible VLA-v4 role model: green citation/URL boxes and red internal-reference boxes, with no cyan boxes.
- No local `paper/main.pdf` remains after export, and no duplicate non-canonical `3.pdf` exists in Downloads.
