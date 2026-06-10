# Reviewer Attacks

## Attack 1: This is just online system identification.
No: the mechanism is a local, potentially discontinuous transition edit with guard scope. It does not assume a low-dimensional global parameter explains the mismatch. The paper should cite sys-ID as hostile and keep this distinction sharp.

## Attack 2: This is just residual dynamics learning.
Residual models usually optimize smooth predictive corrections. CCRA can encode a forbidden affordance or replacement transition that immediately changes planner rollouts, including discontinuities.

## Attack 3: This is just MPC with a learned model.
MPC is the consumer of the model, not the contribution. The contribution is the repair operation induced by planner-execution counterexamples.

## Attack 4: Why not use uncertainty or ensembles?
Uncertainty may help choose actions, but it does not by itself rewrite the false transition the planner will exploit. The ablation should show uncertainty-like caution is not the same as a patch.

## Attack 5: The evidence is toy.
True. The honest claim is mechanistic and diagnostic, not SOTA robotics performance. The paper should be positioned as a minimal mechanism paper and likely workshop/revise unless expanded with real robot or high-fidelity sim evidence.

## Attack 6: The repair memory will overfit.
Yes, if guards are too narrow or stale. The paper should include support counts, exact-scope claims only, and retirement/invalidation as future work unless implemented.

## Attack 7: Prediction loss is a strawman because control papers evaluate task success.
The attack is fair. The paper should avoid saying everyone only optimizes prediction. The narrower point is that world-model updates and benchmarks often still reward average predictive fidelity, while sparse planner-exploited errors need a different update target.

## Attack 8: Active learning already collects failures.
Collecting data is not enough; the core loop is immediate planner-facing transition repair before retraining.

## Attack 9: Verifiers or shielding already prevent bad actions.
A detached shield can block an action, but the novelty claim is updating the transition model so subsequent multi-step planning searches a different physical future.

## Attack 10: The formal lemma is trivial.
It is intentionally simple. Its role is to pin down the mechanism, not to be a deep theorem. The paper must lean on empirical decoupling of prediction loss and task success.
