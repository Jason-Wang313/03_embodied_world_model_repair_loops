# Recovery Notes

Paper 03 attempts 1 and 2 failed mechanically, not scientifically.

- Attempt 1 failed on a brittle inline `python -c` diagnostic with nested quoting.
- Attempt 2 completed the literature synthesis and wrote the runnable evidence artifacts, then the child command wrapper timed out (`exit 124`) while running `python scripts/run_evidence.py`.
- Recovery attempt 1 reused the literature/evidence artifacts, wrote `paper/main.tex` and `paper/references.bib`, then failed mechanically when `latexmk` exited nonzero before producing a usable PDF.

Valid artifacts to reuse:

- `docs/related_work_matrix.csv` with 1,016 rows.
- `docs/literature_map.md`
- `docs/hostile_prior_work.md`
- `docs/novelty_boundary_map.md`
- `docs/novelty_decision.md`
- `docs/claims.md`
- `docs/reviewer_attacks.md`
- `docs/hidden_assumptions.md`
- `docs/literature_synthesis_summary.md`
- `docs/evidence_report.md`
- `src/repair_loop_sim.py`
- `scripts/synthesize_literature.py`
- `scripts/run_evidence.py`
- `results/evidence_trials.csv`
- `results/evidence_summary.json`
- `results/evidence_summary.tex`
- `results/repair_loop_results.svg`
- `paper/figures/results_table.tex`

Evidence summary:

- 80 seeded sparse-contact grid worlds.
- Nominal no-repair first-episode success: 0.00.
- Prediction-gated repair first-episode success: 1.00 with 8.0 mean first-episode counterexamples.
- CCRA exact guard first-episode success: 1.00 with 1.0 mean first-episode counterexamples.
- CCRA row guard first-episode success: 1.00 with 1.0 mean first-episode counterexamples, despite worse full-transition prediction error than nominal.

Resume instructions:

1. Inspect and trust the artifacts above unless a direct consistency check fails.
2. Do not rerun `scripts/run_evidence.py` unless necessary. If rerunning, use an explicit command timeout of at least 300000 ms.
3. Continue from the existing `paper/main.tex` and `paper/references.bib`; patch them if needed instead of rewriting from scratch.
4. Build from the `paper` directory with direct `pdflatex`/`bibtex` passes and a generous timeout. Avoid `latexmk` as the primary build path on this Windows host.
5. Continue with claim tightening, PDF build to `C:/Users/wangz/Downloads/03.pdf`, public GitHub push, and `docs/final_audit.md`.
