# Paper 03 Full-Scale Execution Plan

## Current Claim

The current v2 paper claims that embodied world models sometimes need immediate planner-facing repair loops induced by execution counterexamples, not only lower average next-state prediction loss. The mechanism is Counterexample-Conditioned Repair Automata (CCRA): guarded transition patches installed after the robot observes that a modeled state-action outcome is false. The present evidence is a deterministic sparse-contact grid proxy: nominal prediction error is low but task success is zero because the planner repeatedly exploits a rare false transition; exact CCRA blocks that transition after one mismatch; row-guard CCRA solves the task while worsening global prediction error.

The claim must stay narrow and honest. Exact CCRA in the deterministic exact-guard setting is equivalent to threshold-one transition blocking. The defensible final claim is not that CCRA is a sophisticated new learner. The defensible claim is that a robot needs a planner-facing repair contract that is evaluated by repeated-exploit prevention, counterexample latency, guard scope, feasibility under stale patches, and control-weighted consequence, not only by average transition prediction error.

## Current Gaps

- The manuscript is only about 7 pages and still carries v2 submission-hardening language.
- The evidence is small: 80 seeds, one grid size, one fault type, one route structure, five episodes, and a few baselines.
- The current simulator does not test irrelevant prediction errors, planner horizon, map topology, stochastic contradictions, nonstationary faults, stale-patch retirement, support counts, or guard precision/recall.
- The current threshold sweep is useful but too narrow; it only varies mismatch count in the exact deterministic setting.
- The row guard demonstrates over-repair but does not quantify false-block rate, guard precision, overgeneralization cost, or recovery under stale patches.
- The paper has no large-scale tables, no robust stress figures, no extensive ablations, no failure taxonomy, and no artifact map.
- No real-robot or high-fidelity simulation evidence is available locally. This must remain an explicit limitation rather than be implied away.

## Target Experiments

Build a RAM-light full-scale runner, likely `scripts/run_full_scale_repair_loops.py`, that streams compact rows to `results/full_scale/` and writes paper-ready tables/figures. The runner should preserve the existing simulator as a compatibility layer where possible, but it can add a richer self-contained transition-system generator if that keeps the implementation clearer.

Run these suites:

1. Critical sparse-fault grid suite
   - Vary grid size, number of shortcut faults, fault placement, obstacle density, and planner horizon.
   - Measure first-episode success, all-episode success, repeated exploit count, counterexample latency, steps, replans, patch count, and final prediction error.
   - Purpose: make the original phenomenon robust across map sizes and route structures.

2. Prediction-loss decoupling suite
   - Add many irrelevant off-route transition errors while keeping one sparse on-route false affordance.
   - Compare global prediction error, route-weighted/control-weighted prediction error, and task success.
   - Purpose: show that unweighted average prediction loss can rank models differently from embodied usefulness.

3. Threshold and delayed-repair suite
   - Sweep mismatch thresholds from 1 to at least 32.
   - Include threshold policies that update only after repeated exact state-action mismatches and policies that require repeated local-region mismatches.
   - Purpose: quantify embodied failures paid before a delayed predictor changes the planner-facing model.

4. Guard-scope suite
   - Compare exact, row, column, local-neighborhood, action-wide, region, and learned-from-support guard proxies.
   - Track guard precision, guard recall, false-block rate, extra path length, unreachable-plan rate, and success.
   - Purpose: turn over-repair from a single anecdote into a measured design frontier.

5. Nonstationary/stale-patch suite
   - Faults disappear, move, or switch after a fixed number of episodes.
   - Compare no retirement, TTL retirement, support-count decay, recency-weighted validation, and oracle retirement.
   - Purpose: answer the reviewer attack that repair memory overfits and becomes stale.

6. Stochastic contradiction suite
   - Fault edges fail with probability `p` rather than deterministically.
   - Compare one-mismatch blocking, threshold blocking, confidence/credible-count blocking, and support-weighted CCRA.
   - Purpose: separate deterministic exact-guard guarantees from stochastic repair tradeoffs.

7. Planner-exploitation stress suite
   - Generate maps with false shortcuts of varying attractiveness: no alternative, long detour, short detour, multiple shortcuts, and deceptive corridors.
   - Vary planning horizon and replanning frequency.
   - Purpose: show when sparse false affordances matter and when repair cannot save an infeasible task.

8. Batch retrain versus planner-facing patch suite
   - Simulate a global transition learner that absorbs observed contradictions but only updates after episode boundaries or with smoothing.
   - Compare immediate planner-facing patching, delayed global retraining, and a hybrid patch-plus-consolidation baseline.
   - Purpose: keep the distinction from generic online learning concrete.

## Baselines

At minimum include:

- nominal no-repair;
- oracle true transition model;
- exact CCRA/one-mismatch blocking;
- CCRA with support counts;
- CCRA with TTL or retirement;
- row/region/broad-guard CCRA;
- prediction-gated repair with thresholds;
- delayed batch retraining;
- global frequency transition learner;
- uncertainty/cautious planner that avoids low-confidence transitions without rewriting the model;
- shield-only blocker that blocks the next action but does not update planner rollouts;
- residual/global-bias repair when the environment has a global fault pattern;
- route-weighted prediction-loss repair if feasible.

## Ablations

- Threshold: 1, 2, 4, 8, 16, 32.
- Guard scope: exact, row, column, local radius 1/2/3, region, action-wide, all-fault-family.
- Patch priority: newest-first versus oldest-first and exact-before-broad versus broad-before-exact.
- Retirement: none, TTL, support decay, validation probes, oracle retirement.
- Fault density: 1, 2, 3, 5, 8 faults.
- Fault criticality: on-route, near-route, off-route, false shortcut, mixed.
- Planner horizon or route cost: short/medium/long detours, no alternative.
- Stochastic failure probability: 0.1 through 1.0.
- Irrelevant prediction noise: none, low, medium, high.
- Seed count and episode count sensitivity.

## Stress Tests

- Large seed sweeps with streamed rows, targeting at least hundreds of thousands of compact baseline evaluations.
- Larger grids, e.g. 15x9 through 45x27, without storing full trajectories.
- Many environment families run sequentially to keep RAM flat.
- Edge cases: no valid alternative route, all rightward actions faulty in a row, high false-block broad guard, moving fault, contradictory observations, stochastic single failures, and off-route noise dominating average prediction error.
- Negative controls where prediction loss and task success agree, to avoid overstating the decoupling claim.

## Figures And Tables

Generate paper-local figure copies under `paper/figures/` and generated tables under `paper/tables/`.

Planned figures:

- success versus repeated counterexamples across baselines;
- prediction error versus task success scatter/pareto frontier;
- threshold-delay curve;
- guard-scope precision/recall versus success;
- stale-patch retirement curve;
- stochastic-fault success versus false-block rate;
- planner-exploitation stress heatmap;
- full-scale leaderboard.

Planned tables:

- baseline mechanism/access table;
- main full-scale leaderboard;
- threshold ablation table;
- guard-scope ablation table;
- nonstationary retirement table;
- stochastic contradiction table;
- failure taxonomy and acceptance-boundary table.

## Writing Expansion

Rewrite `paper/main.tex` into a genuine final manuscript of at least 25 pages, targeting 26-28 pages without padding. The expanded paper should include:

- a revised abstract without v2 governance language;
- a sharper introduction centered on planner-facing transition contracts;
- a hostile related-work section covering learned dynamics/MPC, visual foresight, online system ID, residual dynamics, model reconciliation, shielding/verifiers, active learning, and robot foundation-model planning;
- formal definitions for nominal model, true transition, planner-facing patch, guard scope, repeated exploit, control-weighted prediction error, stale patch, and repair latency;
- the exact-guard no-repeat lemma plus a theorem/proposition on threshold delay in deterministic settings;
- an explicit equivalence result: exact CCRA equals one-mismatch blocking under deterministic exact guards;
- a guard-scope design section;
- a nonstationarity and retirement section;
- full experimental protocol with all suites and metrics;
- large results section with figures and tables;
- negative controls and failure cases;
- limitations that clearly state no hardware, no high-dimensional perception, no learned guard formation, and no 3D contact;
- reproducibility and artifact appendix.

## Page-Count Strategy

Target 26-28 pages after normal ICLR formatting. Use the main text for the core claim, formal mechanism, protocol, and strongest results. Use appendices for derivations, simulator details, suite definitions, baseline equations, additional tables, failure cases, negative controls, and artifact maps. Do not use blank pages, formatting tricks, or repetition. The length must come from real experiments, formal clarification, figures, tables, and honest limitations.

## RAM-Light Execution Strategy

- Stream rows directly to CSV and JSON summaries; do not keep raw trajectories in memory.
- Store only aggregate metrics and compact per-run rows.
- Run suites sequentially rather than in parallel.
- Use deterministic standard-library simulation unless a small plotting dependency is already available.
- Reuse computed CSVs with a `--summarize-only` path.
- Generate figures from compact CSV summaries.
- Avoid loading `docs/related_work_matrix.csv` unless necessary for text edits; use existing synthesis docs instead.
- Keep large arrays out of memory; compute prediction error by iterating states/actions.

## Final Acceptance Checklist

- Existing v2 evidence reproduced or intentionally superseded.
- Detailed full-scale runner added with a summarize-only mode.
- Full-scale results produce at least hundreds of thousands of compact baseline-evaluation rows.
- Main manuscript is rewritten into a final 25+ page paper with real content.
- Claims are narrowed around planner-facing repair obligations and transition-contract evaluation.
- Equivalence to one-mismatch blocking in exact deterministic settings is explicit.
- No hardware or high-fidelity robot validation is implied.
- PDF builds cleanly with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` if `latexmk` is unavailable.
- Local PDF is verified by `pdfinfo` and `pdftotext`.
- No PDF is copied to Downloads before the final gate.
- Final PDF copied to `C:\Users\wangz\Downloads\03.pdf` only after final verification.
- Downloads PDF verified as the actual paper and at least 25 pages.
- Docs/logs/reproducibility materials updated to v3 final status.
- Local generated `paper/main.pdf` removed after final copy.
- Repo clean, committed, pushed, and upstream verified before moving to Paper 04.
