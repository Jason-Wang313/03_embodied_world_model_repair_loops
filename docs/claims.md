# Claims Ledger

| ID | Claim | Current support | Status |
| --- | --- | --- | --- |
| C1 | Average next-state prediction loss can be a poor proxy for task success when sparse transition errors lie on planner-preferred routes. | In the v3 planner-exploitation stress suite, nominal and shield-only have 0.00 success with low final prediction error 0.003 and 252.3 first-episode counterexamples. | Supported in the implemented finite-grid evidence; not claimed for all robot domains. |
| C2 | A planner-facing local repair patch can prevent repeated exploitation of the exact same false transition after one observed counterexample in a deterministic finite model with exact guards. | Exact CCRA reaches 1.00 stress success with 1.0 first-episode counterexample; formal no-repeat lemma in paper. | Formally supportable under narrow deterministic exact-guard assumptions. |
| C3 | Immediate planner-facing repair can improve success with fewer deployment failures than delayed mismatch-count gating. | Threshold suite: thresholds 1, 2, 4, 8, 16, 32 pay exactly 1.0, 2.0, 4.0, 8.0, 16.0, 32.0 first-episode counterexamples. | Supported in the implemented suites; threshold 1 is equivalent to exact CCRA. |
| C4 | Guard scope is a central design frontier. | Guard-scope suite: exact/local/row guards can solve; action/global guards fail; row guard stress false-block rate 0.87. | Supported in the implemented suites; learned guards are not solved. |
| C5 | Repair memory needs lifecycle management under nonstationarity. | Nonstationary suite: exact CCRA succeeds but stale false-block rate reaches 0.37; TTL/oracle retirement reduce false blocks. | Supported in generated nonstationary settings. |
| C6 | The contribution is not online system identification because repairs can be discontinuous local transition overrides rather than global parameter estimates. | Literature boundary plus mechanism definition. | Supported as a positioning claim. |
| C7 | The paper does not establish scalability to high-dimensional perception, tactile manipulation, deformable objects, or real robot foundation models. | No real-robot or high-fidelity simulator experiment is included. | Limitation; must remain explicit. |
| C8 | Exact CCRA is not algorithmically distinct from one-mismatch transition blocking in deterministic exact-guard grids. | Threshold-1 baseline and exact CCRA are behaviorally equivalent in the deterministic exact-guard setting. | Limitation; must remain explicit. |

## Formal Claim Scope

The main formal claims are narrow: exact-guard no-repeat, threshold-delay, and a finite prediction-error/task-success decoupling construction. The paper may claim that repeated mismatch-count thresholds trade embodied failures for delayed repair in these generated settings, but it must also state that threshold-one blocking collapses to exact CCRA under deterministic exact guards.
