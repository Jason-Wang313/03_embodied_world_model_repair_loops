# Novelty Boundary Map

## Not Novel Enough
- A larger video/world model for robot prediction.
- Lower next-frame, latent-dynamics, or reconstruction loss alone.
- Standard MPC with a learned dynamics model.
- Online system identification as global parameter fitting.
- Residual dynamics on top of a nominal simulator.
- Adding uncertainty, ensembles, active learning, or a verifier without changing the planner-facing transition relation.
- LLM/foundation-model planning with existing robot skills.
- A benchmark that exposes model errors without a new repair mechanism.

## Crowded Mechanisms In The Top 300
| Cluster | Top-300 count | Boundary imposed |
| --- | ---: | --- |
| learned dynamics + MPC | 161 | Planning with learned dynamics is not new; the paper must change the update target and trigger distribution. |
| contact / tactile dynamics | 131 | Planning with learned dynamics is not new; the paper must change the update target and trigger distribution. |
| sim-to-real transfer | 78 | Training-time coverage is not enough; the contribution must operate during deployment after unexpected mismatch. |
| curiosity / active exploration | 51 | This cluster constrains broad claims; keep the central claim narrowly about repair loops. |
| movement primitives / skill models | 35 | This cluster constrains broad claims; keep the central claim narrowly about repair loops. |
| uncertainty / ensembles | 19 | Adding uncertainty alone is weak; the repair should be triggered by embodied contradictions and planner dependency. |
| foundation / language-conditioned robotics | 17 | Language/foundation planning is not new; grounded repair must override semantic priors. |
| object-centric / scene graphs | 14 | This cluster constrains broad claims; keep the central claim narrowly about repair loops. |
| visual foresight / video prediction | 12 | Next-frame or future-image quality is heavily occupied; novelty must be about how failures rewrite planner-facing transitions. |
| residual correction | 8 | Residual correction is crowded; discontinuous guarded patches need to be central and justified. |
| online system identification | 7 | Online adaptation is not new; novelty requires local structural repairs beyond global parameter estimation. |
| other embodied model/control priors | 1 | This cluster constrains broad claims; keep the central claim narrowly about repair loops. |

## Open Boundary
The least occupied contribution shape is a control-centered repair loop: after the robot executes an action and observes a contradiction, the system creates a scoped patch to the transition relation used by the planner. The patch is not a generic confidence score, not a detached verifier, and not batch retraining. It is an immediate change to what future rollouts are allowed to assume.

## Minimum Novel Claim That Survives The Hostile Set
Given the surveyed prior work, the defensible claim is narrow: in sparse critical-mismatch regimes, planner-triggered local transition repair can improve embodied task success while leaving average prediction loss unimproved or even worse than a prediction-centric updater. This changes the central mechanism and metric from predictive fidelity to preventing repeated plan exploitation of false affordances.
