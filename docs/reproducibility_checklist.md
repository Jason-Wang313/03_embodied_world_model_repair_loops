# Reproducibility Checklist

## Environment

- Simulator uses Python standard library.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.

## Commands

```powershell
python scripts/smoke_test.py
python scripts/run_evidence.py
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Expected Outputs

- `results/evidence_trials.csv`
- `results/evidence_summary.csv`
- `results/evidence_summary.json`
- `results/threshold_sweep.csv`
- `results/repair_loop_results.svg`
- `paper/figures/results_table.tex`
- `paper/figures/threshold_table.tex`
- `paper/main.pdf`
- `C:/Users/wangz/Downloads/03.pdf`

## Known Non-Reproducible Pieces

- Literature sweep depends on external scholarly metadata if rerun.
- No hardware data exists.
- Evidence run takes several minutes on this machine.
