# Embodied World Model Repair Loops

Anonymous ICLR-style paper artifact for paper 03 in the robotics/embodied-intelligence batch.

## Thesis

Robot world models should sometimes be updated by planner-facing repair loops induced by execution counterexamples, not by optimizing average next-state prediction quality alone. The central mechanism is Counterexample-Conditioned Repair Automata (CCRA): guarded transition patches that are installed after the robot observes that a planned action's modeled effect is false.

The final v3 claim is deliberately narrow: exact CCRA is equivalent to one-mismatch blocking under deterministic exact guards. The contribution is the planner-facing transition-contract repair target and its evaluation by repeated-exploit prevention, repair latency, guard scope, false-block rate, stale patch behavior, and prediction-success decoupling.

## Repository Layout

- `paper/main.tex` - anonymous ICLR-style final manuscript.
- `paper/references.bib` - bibliography.
- `src/repair_loop_sim.py` - original deterministic sparse-contact repair-loop simulator.
- `scripts/run_evidence.py` - original v2 evidence run.
- `scripts/run_full_scale_repair_loops.py` - v3 full-scale streamed runner.
- `scripts/smoke_test.py` - fast simulator sanity check.
- `docs/related_work_matrix.csv` - 1,016-paper literature matrix.
- `docs/*` - novelty, adversarial audit, readiness, and reproducibility artifacts.
- `results/full_scale/` - corrected v3 full-scale results.
- `paper/figures/` and `paper/tables/` - generated manuscript figures/tables.

## Reproduce Evidence

```powershell
python scripts\smoke_test.py
python scripts\run_evidence.py
python scripts\run_full_scale_repair_loops.py --seed-scale 20
python scripts\run_full_scale_repair_loops.py --summarize-only
```

The v3 full-scale run writes 34,880 compact per-episode rows across seven suites and stores no raw trajectories.

## Build Paper

```powershell
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Current Evidence Snapshot

- Corrected full-scale rows: 34,880.
- Planner-exploitation stress: nominal and shield-only have 0.00 success despite final prediction error 0.003.
- Exact CCRA reaches 1.00 stress success after 1.0 first-episode counterexample.
- Threshold-8 reaches 1.00 stress success but pays 8.0 first-episode counterexamples.
- Row guards solve but over-block: false-block rate 0.87 and control-weighted error 0.264.
- Guard-scope suite shows exact/local/row guards can solve, while action/global guards fail from overgeneralization.
- Nonstationary suite shows stale false blocks without retirement.

The final local manuscript build is 25 pages. The canonical batch PDF is copied to `C:/Users/wangz/Downloads/03.pdf` only after final verification.
