# Claims Ledger

| ID | Claim | Current support | Status |
| --- | --- | --- | --- |
| C1 | Average next-state prediction loss can be a poor proxy for task success when sparse transition errors lie on planner-preferred routes. | In 80 seeded sparse-contact worlds, nominal no-repair has only 0.004 average transition error but 0.00 first-episode success. The broad row-guard CCRA has worse final full-transition prediction error (0.022) but 1.00 first-episode success. | Supported in the implemented finite-grid evidence; not claimed for all robot domains. |
| C2 | A planner-facing local repair patch can prevent repeated exploitation of the exact same false transition after one observed counterexample in a deterministic finite model with exact guards. | Direct proof sketch in the paper plus implementation behavior: exact CCRA reaches 1.00 first-episode success with 1.0 mean first-episode counterexample. | Formally supportable under narrow deterministic exact-guard assumptions. |
| C3 | Immediate planner-facing repair can improve success with fewer deployment failures than delayed mismatch-count gating in sparse mismatch settings. | Prediction-gated repair with threshold 8 reaches 1.00 first-episode success after 8.0 mean first-episode counterexamples; exact and row-guard CCRA reach 1.00 after 1.0. | Supported in the implemented toy setting; threshold 1 is equivalent to exact CCRA. |
| C4 | The contribution is not online system identification because repairs can be discontinuous local transition overrides rather than global parameter estimates. | Literature boundary from the hostile set and mechanism definition. | Supported as a positioning claim. |
| C5 | The contribution is not uncertainty, active learning, or verifier-only robotics because the update directly changes the transition model used in future planning. | Mechanism definition and ablations separate no-repair, delayed prediction-gated repair, exact repair, broad repair, and oracle. | Supported for the implemented mechanism comparison. |
| C6 | The paper does not establish scalability to high-dimensional perception, tactile manipulation, deformable objects, or real robot foundation models. | No real-robot or high-fidelity simulator experiment is included. | Limitation; must remain explicit. |
| C7 | Exact CCRA is not algorithmically distinct from one-mismatch transition blocking in the deterministic exact-guard grid. | `results/threshold_sweep.csv` shows threshold 1 reaches 1.00 success with 1.0 counterexample and the same final prediction error as exact CCRA. | Limitation; must remain explicit. |

## Formal Claim Scope

The only formal claim intended for the main paper is the exact-guard no-repeat lemma: in a deterministic finite transition system, if an executed state-action pair contradicts the nominal model and the repair patch exactly matches that state-action pair, a planner using the patched model will not choose a plan whose validity depends on the old transition for that same guarded pair, unless no alternative plan exists or the planner ignores the patch. This is deliberately narrow.

Submission-hardening v2 adds a threshold sweep. The paper may claim that repeated mismatch-count thresholds trade embodied failures for delayed repair in this toy setup, but it must also state that threshold-one blocking collapses to exact CCRA.
