# Reviewer Attacks

## Attack 1: This is just online system identification.

No: the mechanism is a local, potentially discontinuous planner-facing transition edit with guard scope. It does not assume a low-dimensional global parameter explains the mismatch. The paper should cite sys-ID as hostile and keep this distinction sharp.

## Attack 2: This is just residual dynamics learning.

Residual models usually optimize smooth predictive corrections. CCRA can encode a forbidden affordance or replacement transition that immediately changes planner rollouts, including discontinuities.

## Attack 3: This is just MPC with a learned model.

MPC is the consumer of the model, not the contribution. The contribution is the repair operation induced by planner-execution counterexamples.

## Attack 4: Why not use uncertainty or ensembles?

Uncertainty may help choose actions. The v3 cost-avoidance baseline is intentionally strong and often solves. This supports the broader planner-facing repair claim while distinguishing cost repair from transition replacement.

## Attack 5: The evidence is toy.

True. The honest claim is mechanistic and diagnostic, not SOTA robotics performance. The final paper is a 25-page simulation/mechanism manuscript with a corrected 34,880-row pass, not a hardware result.

## Attack 6: The repair memory will overfit.

Yes, if guards are too broad or stale. The v3 guard-scope and nonstationary retirement suites measure false-block rate and stale patch behavior directly.

## Attack 7: Prediction loss is a strawman because control papers evaluate task success.

The attack is fair. The paper should avoid saying everyone only optimizes prediction. The narrower point is that world-model updates and benchmarks often still reward average predictive fidelity, while sparse planner-exploited errors need a different update target.

## Attack 8: Active learning already collects failures.

Collecting data is not enough; the core loop is immediate planner-facing transition repair before retraining.

## Attack 9: Verifiers or shielding already prevent bad actions.

A detached shield can block an action, but the novelty claim is updating the transition model so subsequent multi-step planning searches a different physical future. The v3 shield-only baseline fails like nominal in the stress suite.

## Attack 10: The formal lemma is trivial.

It is intentionally simple. Its role is to pin down the mechanism, not to be a deep theorem. The paper leans on empirical decoupling, threshold delay, guard-scope, stale-patch, and stochastic stress results.

## Attack 11: Exact CCRA is just blocking a failed transition after one mismatch.

Concede. The threshold sweep shows threshold 1 is behaviorally equivalent to exact CCRA in the deterministic grid. The defensible contribution is the planner-facing repair obligation and evaluation target, not a complicated algorithm.

## Attack 12: The oracle/planner might be weak.

This was caught and fixed before the final manuscript. The final runner uses set-based A* over known blocked transitions, so oracle success is a valid upper bound in the generated grids.
