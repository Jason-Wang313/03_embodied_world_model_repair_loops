# Experiment Rigor Checklist

| Item | Status | Evidence |
|---|---|---|
| Multiple seeds | Done | 80 seeded environments. |
| Multiple episodes | Done | 5 deployment episodes per method. |
| Main baselines | Done | Nominal, prediction-gated, exact CCRA, row CCRA, oracle. |
| Threshold ablation | Done | `results/threshold_sweep.csv`. |
| Uncertainty estimates | Partial | CI fields for counterexamples and final prediction error. |
| Failure case | Done | Nominal repeatedly exploits sparse false transition. |
| Stress beyond grid | Missing | No stochastic/continuous/high-fidelity task. |
| Real robot | Missing | Non-recoverable locally. |
| Claims narrowed to evidence | Done | Paper, final audit, and reviewer responses updated. |

## Rigor Decision

Adequate for a workshop mechanism paper. Not adequate for main-conference robotics/world-model claims.
