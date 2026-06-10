# Plan: Paper 03 - Embodied World Model Repair Loops

## Operating rules
- Stay inside the assigned robotics / embodied-intelligence field box.
- Treat the seed as a hypothesis, not a conclusion.
- Reuse any valid artifacts already present in this retry folder.
- Keep `child_status.md` compact and current with stage, commands, failures, and recovery.
- Use safe, non-interactive commands with explicit timeouts for long work.
- Do not let status-update failures abort the run.

## Execution stages
1. Inspect existing repo state and reusable artifacts.
2. Build or refresh the literature pipeline:
   - 1000-paper landscape sweep into `docs/related_work_matrix.csv`.
   - 300-paper serious skim.
   - 200-250-paper deep read.
   - 100-paper hostile prior-work set.
3. Analyze field assumptions:
   - Define the field box.
   - Extract mechanisms, fixed variables, hidden assumptions, ignored failures, novelty pressure, and open gaps.
   - Identify at least 20 potentially false assumptions.
4. Choose the strongest thesis only after the sweep:
   - Compare candidate mechanisms against hostile prior work.
   - Write `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, `docs/novelty_decision.md`, `docs/claims.md`, and `docs/reviewer_attacks.md`.
5. Produce runnable evidence:
   - Implement a small, cached experiment around online model repair loops in an embodied-control setting.
   - Generate plots/tables from scripts with progress output and bounded runtime.
6. Write the anonymous ICLR-style paper using the latest official template available at runtime.
7. Compile the final PDF and save it only to `C:/Users/wangz/Downloads/03.pdf`.
8. Create/push the public GitHub repo `03_embodied_world_model_repair_loops`, or document the exact failure.
9. Write `docs/final_audit.md` answering all required audit questions, including PDF path, GitHub URL, and desktop-copy status.

## Initial commands to run safely
- `Get-ChildItem -Force`
- `git status --short`
- `Get-ChildItem -Recurse -Depth 2`
- Tool availability checks with `Get-Command`, not version probes.

## Completion condition
Do not stop until the repo is runnable, the paper is compiled or the failure is documented, the GitHub push is complete or the failure is documented, and `docs/final_audit.md` exists.
