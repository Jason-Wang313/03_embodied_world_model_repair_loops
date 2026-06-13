# Reproducibility Checklist

## Environment

- Original simulator uses Python standard library.
- Full-scale runner uses Python plus `matplotlib` for PNG figures.
- LaTeX build: `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.

## Commands

```powershell
python scripts/smoke_test.py
python scripts/run_evidence.py
python scripts/run_full_scale_repair_loops.py --seed-scale 20
python scripts/run_full_scale_repair_loops.py --summarize-only
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
- `results/full_scale/*.csv`
- `results/full_scale/leaderboard.csv`
- `results/full_scale/full_scale_summary.json`
- `paper/figures/*.png`
- `paper/tables/*.tex`
- transient local build `paper/main.pdf`
- final numbered artifact `C:/Users/wangz/Downloads/03.pdf`

## Final Gate

- Full-scale runner writes 34,880 compact per-episode rows and stores no raw trajectories.
- Local final build verified at 25 pages before copying to Downloads.
- Downloads copy allowed only after PDF text is verified as the actual paper.
- After copying, remove transient local `paper/main.pdf`.

## Known Non-Reproducible Pieces

- Literature sweep depends on external scholarly metadata if rerun.
- No hardware data exists.
- No high-fidelity contact simulation exists.
