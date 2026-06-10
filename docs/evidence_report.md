# Evidence Report

Ran `80` seeded sparse-contact grid worlds with `5` deployment episodes per method. The nominal model knows grid boundaries but not sparse one-way contact failures on the shortest route. Each episode repeatedly plans with the current model, executes the first action, and lets the method update from observed contradictions.

## Main Result
- Nominal no-repair first-episode success: 0.00; mean first-episode counterexamples: 114.6; final prediction error: 0.004.
- Prediction-gated repair first-episode success: 1.00; mean first-episode counterexamples: 8.0; final prediction error: 0.002.
- CCRA exact first-episode success: 1.00; mean first-episode counterexamples: 1.0; final prediction error: 0.002.
- CCRA row-guard first-episode success: 1.00; mean first-episode counterexamples: 1.0; final prediction error: 0.022.

## Interpretation
The nominal model has low average transition error because the faults are sparse, but the planner repeatedly selects the false shortcut and fails. Immediate repair changes the planner-facing model after the first contradiction. The row-guard variant deliberately makes a broader patch: it can have worse full-transition prediction error than the nominal model while still solving the task, illustrating that prediction quality and embodied usefulness can diverge.

## Files
- `results/evidence_trials.csv`
- `results/evidence_summary.json`
- `results/repair_loop_results.svg`
- `paper/figures/results_table.tex`
