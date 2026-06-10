# Embodied World Model Repair Loops

Anonymous ICLR-style paper artifact for paper 03 in the robotics/embodied-intelligence batch.

## Thesis

Robot world models should sometimes be updated by planner-facing repair loops induced by execution counterexamples, not by optimizing average next-state prediction quality alone. The central mechanism is Counterexample-Conditioned Repair Automata (CCRA): guarded transition patches that are installed after the robot observes that a planned action's modeled effect is false.

## Repository Layout

- `paper/main.tex` - anonymous ICLR-style paper.
- `paper/references.bib` - bibliography.
- `src/repair_loop_sim.py` - deterministic sparse-contact repair-loop simulator.
- `scripts/run_evidence.py` - full evidence run that regenerates results and table files.
- `scripts/smoke_test.py` - fast simulator sanity check.
- `scripts/build_literature_corpus.py` and `scripts/synthesize_literature.py` - literature collection/synthesis scripts.
- `docs/related_work_matrix.csv` - 1,016-paper literature matrix.
- `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, `docs/reviewer_attacks.md` - novelty and adversarial audit artifacts.
- `results/evidence_summary.json`, `results/evidence_trials.csv`, `results/repair_loop_results.svg` - cached evidence outputs.

## Reproduce Evidence

The simulator uses only the Python standard library.

```powershell
python scripts\smoke_test.py
python scripts\run_evidence.py
```

The full run writes:

- `results/evidence_trials.csv`
- `results/evidence_summary.csv`
- `results/evidence_summary.json`
- `results/repair_loop_results.svg`
- `paper/figures/results_table.tex`

## Build Paper

The paper uses the official ICLR 2026 style files from the ICLR Master-Template repository.

```powershell
cd paper
latexmk -pdf -interaction=nonstopmode main.tex
```

The batch deliverable PDF is written to:

```text
C:/Users/wangz/Downloads/03.pdf
```

## Current Evidence Snapshot

Across 80 seeded sparse-contact grid worlds with five deployment episodes per method:

- Nominal no-repair: 0.00 first-episode success, 114.6 first-episode counterexamples, 0.004 final prediction error.
- Prediction-gated repair: 1.00 success, 8.0 counterexamples, 0.002 final prediction error.
- CCRA exact guard: 1.00 success, 1.0 counterexample, 0.002 final prediction error.
- CCRA row guard: 1.00 success, 1.0 counterexample, 0.022 final prediction error.

The row-guard result is intentionally provocative: it solves the task while worsening average full-transition prediction error, showing why planner-facing repair can be a different objective from global predictive fidelity.
