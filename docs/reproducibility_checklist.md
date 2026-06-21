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
- Current canonical artifact after 2026-06-21 VLA highlight hardening: `C:/Users/wangz/Downloads/03.pdf`, 25 pages, 553,427 bytes, SHA256 `3EBEAABFAC96FA12774A6441F4CF1CCDB28DAE78A0F55212AC18AD3585611F8D`.
- Link annotation verification: 79 annotations on pages `[(1, 26), (3, 36), (6, 3), (7, 1), (8, 4), (9, 2), (17, 6), (18, 1)]`; green = 68, red = 11, cyan = 0; all borders `(0, 0, 1)`.
- Visual verification: rendered link-bearing pages 1, 3, 6, 7, 8, 9, 17, and 18; no oversized page-edge annotations.
- Cleanup verification: no duplicate `C:/Users/wangz/Downloads/3.pdf`; local `paper/main.pdf` removed.

## Known Non-Reproducible Pieces

- Literature sweep depends on external scholarly metadata if rerun.
- No hardware data exists.
- No high-fidelity contact simulation exists.
