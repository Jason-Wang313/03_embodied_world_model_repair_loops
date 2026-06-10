# Novelty Decision

## Candidate Directions
| Direction | Broken assumption | Mechanism | Why it is strong | Risk | Score |
| --- | --- | --- | --- | --- | ---: |
| Counterexample-conditioned transition repair | Prediction loss is a proxy for decision usefulness. | Execution failures become guarded transition patches used immediately by the planner. | Changes the central object from future generation to planner-facing repair obligations. | Toy evidence may not prove scalability to high-dimensional perception. | 9 |
| Repair-scope calculus for stale embodied patches | Deployment environments are stationary. | Repairs carry support, invalidation tests, and retirement conditions. | Attacks a real deployment issue but is secondary without a core repair loop. | May look like cache invalidation or continual-learning hygiene. | 7 |
| Planner-exploitation benchmark for world models | One-step accuracy determines long-horizon utility. | Adversarially searches for state-action errors that a planner will exploit. | Useful diagnostic but benchmark-only is forbidden unless paired with a new mechanism. | Could be reviewed as new benchmark only. | 6 |
| Latent-to-symbol repair distillation | Latents preserve repair-relevant causal variables. | Distills failure-triggered latent differences into guard predicates. | Could bridge foundation models and planning. | Too broad for this paper without heavy perception experiments. | 5 |

## Chosen Thesis
Embodied world models should be evaluated and updated through repair loops induced by robot execution counterexamples, not only through next-state prediction quality. A planner-facing world model needs a mechanism for immediately installing scoped transition patches when the robot discovers that a planned action's assumed effect is false.

## Chosen Mechanism
Counterexample-Conditioned Repair Automata (CCRA): a nominal action model plus an ordered set of guarded transition patches. Each patch stores a state-action guard, an observed replacement outcome or forbidden affordance, support counts, and a planner-facing obligation. Planning rolls out the patched model. Execution failures add or strengthen patches. Exact repeated exploitation is eliminated in deterministic finite environments when guards are exact.

## Why This Beats The Seed If Needed
The seed said to make online model repair the mechanism instead of next-frame prediction quality. The literature sweep sharpens this: the repair must be planner-facing, counterexample-conditioned, and local/guarded, because online adaptation and residual learning already cover many weaker versions of repair.
