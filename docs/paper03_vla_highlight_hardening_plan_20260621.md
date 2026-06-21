# Paper03 VLA Highlight Hardening Plan

Date: 2026-06-21

## Objective

Make `C:/Users/wangz/Downloads/03.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 25-page embodied
world-model repair-loops paper:

- citation links use green one-point boxes;
- internal figure/table/equation/section links use red one-point boxes;
- URL links use green one-point boxes;
- no cyan or oversized link boxes appear;
- the final PDF is rebuilt, copied to Downloads, visually checked, and leaves
  no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/03.pdf`
- Pages: 25
- Size: 553,427 bytes
- SHA256: `2884A4945F25558CD3E211597E9BF87246C885ABBFBFA2A09C99E6AF98C9035A`
- Local `paper/main.pdf`: absent
- Repository branch: `master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(1, 26), (3, 36), (6, 3), (7, 1), (8, 4), (9, 2), (17, 6), (18, 1)]`
- Annotation colors: green = 68, red = 11, cyan = 0
- Border widths: `(0, 0, 1)` for all link annotations
- Oversized annotation audit: 0 malformed page-edge rectangles

Source finding:

- `paper/main.tex` is the active manuscript source.
- The active manuscript already loads `hyperref`, and the baseline PDF already
  has green citation/URL boxes and red internal-reference boxes.
- The source does not explicitly pin the VLA-v4 `\hypersetup` policy, so this
  pass will make the matching behavior explicit and auditable.
- Use the documented manual LaTeX flow from `paper/`: `pdflatex`, `bibtex`,
  and repeated `pdflatex` passes before export.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block in the active `paper/main.tex` preamble
   immediately after the existing `\usepackage{hyperref}`.
2. Rebuild manually from `paper/` with `pdflatex`, `bibtex`, and repeated
   `pdflatex` passes.
3. If the log asks for another pass for cross-references, run the final
   canonical pass before recording metadata.
4. Copy the rebuilt `paper/main.pdf` to `C:/Users/wangz/Downloads/03.pdf`.
5. Remove local `paper/main.pdf` after export.
6. Recompute page count, byte size, SHA256, annotation colors, border widths,
   link pages, and oversized annotation count from the final Downloads PDF.
7. Render every page that contains final link annotations into
   `tmp/pdfs/paper03_after`.
8. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan or oversized page-edge boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
9. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
10. Validate build logs, diff hygiene, final PDF hash, expected claim markers,
    and absence of local `paper/main.pdf`.
11. Remove Paper03 temp renders, leaving only the shared role-model render
    directory.
12. Stage only Paper03 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper02.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, URLs, or template examples merely
  to change link counts.
- Do not create an additional `3.pdf`; keep the repository's canonical
  Downloads target as `03.pdf`.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

Completed source/build/export actions:

- Added the explicit VLA-v4 `\hypersetup` block immediately after `\usepackage{hyperref}` in `paper/main.tex`.
- Rebuilt from `paper/` with manual `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` passes.
- Copied the verified build to `C:/Users/wangz/Downloads/03.pdf`.
- Removed transient local `paper/main.pdf` after export.

Final canonical artifact:

- PDF: `C:/Users/wangz/Downloads/03.pdf`
- Pages: 25
- Size: 553,427 bytes
- SHA256: `3EBEAABFAC96FA12774A6441F4CF1CCDB28DAE78A0F55212AC18AD3585611F8D`

Final link inventory:

- Link pages: `[(1, 26), (3, 36), (6, 3), (7, 1), (8, 4), (9, 2), (17, 6), (18, 1)]`
- Annotation colors: green = 68, red = 11, cyan = 0
- Border widths: `(0, 0, 1)` for all link annotations
- Oversized annotation audit: 0 malformed page-edge rectangles

Visual audit:

- Rendered pages 1, 3, 6, 7, 8, 9, 17, and 18 into the Paper03 temp render folder.
- Inspected the rendered contact sheet: citation and URL boxes are green, internal-reference boxes are red, all boxes are crisp/aligned, and no cyan or page-edge boxes appear.

Cleanup state:

- No duplicate `C:/Users/wangz/Downloads/3.pdf`.
- No local `paper/main.pdf`.
