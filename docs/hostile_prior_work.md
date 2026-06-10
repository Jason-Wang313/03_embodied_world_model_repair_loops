# Hostile Prior Work

This file lists the 100-paper hostile set from the matrix. These are the papers most likely to make a broad version of the proposed contribution sound already done. Each entry preserves the required extraction fields from `docs/related_work_matrix.csv`.

## 1. Transfer from Simulation to Real World through Learning Deep Inverse Dynamics Model (2016)
- Authors: Paul F. Christiano; Zain Shah; Igor Mordatch; Jonas Schneider; Trevor Blackwell; Joshua Tobin; Pieter Abbeel; Wojciech Zaremba
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/1610.03518
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling; simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; epistemic uncertainty is calibrated enough to guide action; reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 2. DeepMPC: Learning Deep Latent Features for Model Predictive Control (2015)
- Authors: Ian Lenz; Ross A. Knepper; Ashutosh Saxena
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2015.xi.012
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model; reinforcement-learning objective around a learned model
- Hidden assumptions: the learned latent variables preserve the repair-relevant causal factors; reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime
- Failure modes ignored: unobserved variables changing repair validity
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 3. Self-Supervised Sim-to-Real Adaptation for Visual Robotic Manipulation (2020)
- Authors: Rae Jeong; Yusuf Aytar; David Khosid; Yuxiang Zhou; Jackie Kay; Thomas Lampe; Konstantinos Bousmalis; Francesco Nori
- Venue: 
- URL/DOI: https://doi.org/10.1109/icra40945.2020.9197326
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; the learned latent variables preserve the repair-relevant causal factors; training variation covers deployment mismatches
- Variables treated as fixed: contact/friction regime
- Failure modes ignored: unobserved variables changing repair validity; planner exploitation of small model errors; out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 4. Preparing for the Unknown: Learning a Universal Policy with Online System Identification (2017)
- Authors: Wenhao Yu; Jie Tan; C. Karen Liu; Greg Turk
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2017.xiii.048
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: online or offline identification of dynamics parameters; reinforcement-learning objective around a learned model
- Hidden assumptions: the right repair is expressible as global parameter adaptation; reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 5. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)
- Authors: Wenlong Huang; Chen Wang; Ruohan Zhang; Yunzhu Li; Jiajun Wu; Li Fei-Fei
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/2307.05973
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: large generative/foundation model conditioning; contact/tactile dynamics modeling
- Hidden assumptions: model errors remain tolerable over the planner horizon; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 6. Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control (2018)
- Authors: Frederik Ebert; Chelsea Finn; Sudeep Dasari; Annie Xie; Alex X. Lee; Sergey Levine
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/1812.00568
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight; planning by rolling out a learned or hybrid dynamics model; reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 7. Belief space planning assuming maximum likelihood observations (2010)
- Authors: Robert W. Platt; Russ Tedrake; Leslie Pack Kaelbling; Tomás Lozano‐Pérez
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2010.vi.037
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 8. OpenSim: Simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement (2018)
- Authors: Ajay Seth; Jennifer L. Hicks; Thomas K. Uchida; Ayman Habib; Christopher L. Dembia; James J. Dunne; Carmichael Ong; Matthew S. DeMers
- Venue: PLoS Computational Biology
- URL/DOI: https://doi.org/10.1371/journal.pcbi.1006223
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 9. Developmental robotics, optimal artificial curiosity, creativity, music, and the fine arts (2006)
- Authors: Jürgen Schmidhuber
- Venue: Connection Science
- URL/DOI: https://doi.org/10.1080/09540090600768658
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 10. Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors (2012)
- Authors: Auke Jan Ijspeert; Jun Nakanishi; H. Hoffmann; Peter Pástor; Stefan Schaal
- Venue: Neural Computation
- URL/DOI: https://doi.org/10.1162/neco_a_00393
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 11. A novel type of compliant and underactuated robotic hand for dexterous grasping (2015)
- Authors: Raphael Deimel; Oliver Brock
- Venue: The International Journal of Robotics Research
- URL/DOI: https://doi.org/10.1177/0278364915592961
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 12. Sim-to-Real: Learning Agile Locomotion For Quadruped Robots (2018)
- Authors: Jie Tan; Tingnan Zhang; Erwin Coumans; Atıl Işçen; Yunfei Bai; Danijar Hafner; Steven Bohez; Vincent Vanhoucke
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2018.xiv.010
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: online or offline identification of dynamics parameters; simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: the right repair is expressible as global parameter adaptation; training variation covers deployment mismatches; reward feedback is the main signal for correcting model use
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 13. Gaussian Processes for Data-Efficient Learning in Robotics and Control (2013)
- Authors: Marc Peter Deisenroth; Dieter Fox; Carl Edward Rasmussen
- Venue: IEEE Transactions on Pattern Analysis and Machine Intelligence
- URL/DOI: https://doi.org/10.1109/tpami.2013.218
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model; uncertainty-aware model estimation
- Hidden assumptions: model errors remain tolerable over the planner horizon; epistemic uncertainty is calibrated enough to guide action; reward feedback is the main signal for correcting model use
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; miscalibrated confidence around rare failures
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 14. Large-Area Soft e-Skin: The Challenges Beyond Sensor Designs (2019)
- Authors: Ravinder Dahiya; Nivasan Yogeswaran; Fengyuan Liu; Libu Manjakkal; Etienne Burdet; Vincent Hayward; Henrik Jörntell
- Venue: Proceedings of the IEEE
- URL/DOI: https://doi.org/10.1109/jproc.2019.2941366
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 15. Real-Time Neural MPC: Deep Learning Model Predictive Control for Quadrotors and Agile Robotic Platforms (2023)
- Authors: Tim Salzmann; Elia Kaufmann; Jon Arrizabalaga; Marco Pavone; Davide Scaramuzza; Markus Ryll
- Venue: IEEE Robotics and Automation Letters
- URL/DOI: https://doi.org/10.1109/lra.2023.3246839
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model
- Hidden assumptions: model errors remain tolerable over the planner horizon; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 16. One-shot learning of manipulation skills with online dynamics adaptation and neural network priors (2016)
- Authors: Justin Fu; Sergey Levine; Pieter Abbeel
- Venue: 
- URL/DOI: https://doi.org/10.1109/iros.2016.7759592
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model; reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 17. Safe and Fast Tracking on a Robot Manipulator: Robust MPC and Neural Network Control (2020)
- Authors: Julian Nubert; Johannes Köhler; Vincent Berenz; Frank Allgöwer; Sebastian Trimpe
- Venue: IEEE Robotics and Automation Letters
- URL/DOI: https://doi.org/10.1109/lra.2020.2975727
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 18. Toward Dexterous Manipulation With Augmented Adaptive Synergies: The Pisa/IIT SoftHand 2 (2018)
- Authors: Cosimo Della Santina; Cristina Piazza; Giorgio Grioli; Manuel G. Catalano; Antonio Bicchi
- Venue: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2018.2830407
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 19. VisuoSpatial Foresight for Multi-Step, Multi-Task Fabric Manipulation (2020)
- Authors: Ryan Hoque; Daniel Seita; Ashwin Balakrishna; Aditya Ganapathi; Ajay Kumar Tanwani; Nawid Jamali; Katsu Yamane; Soshi Iba
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2020.xvi.034
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 20. Improvisation through Physical Understanding: Using Novel Objects As Tools with Visual Foresight (2019)
- Authors: Annie Xie; Frederik Ebert; Sergey Levine; Chelsea Finn
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2019.xv.001
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight; reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 21. VisuoSpatial Foresight for Multi-Step, Multi-Task Fabric Manipulation (2020)
- Authors: Ryan Hoque; Daniel Seita; Ashwin Balakrishna; Aditya Ganapathi; Ajay Kumar Tanwani; Nawid Jamali; Katsu Yamane; Soshi Iba
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/2003.09044
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 22. VisuoSpatial Foresight for Physical Sequential Fabric Manipulation (2021)
- Authors: Ryan Hoque; Daniel Seita; Ashwin Balakrishna; Aditya Ganapathi; Ajay Kumar Tanwani; Nawid Jamali; Katsu Yamane; Soshi Iba
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/2102.09754
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 23. The vector field histogram-fast obstacle avoidance for mobile robots (1991)
- Authors: J. Borenstein; Yoram Koren
- Venue: IEEE Transactions on Robotics and Automation
- URL/DOI: https://doi.org/10.1109/70.88137
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of using action-conditioned prediction as a robot world model.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 24. A Comprehensive Survey of Multiagent Reinforcement Learning (2008)
- Authors: Lucian Buşoniu; Robert Babuška; Bart De Schutter
- Venue: IEEE Transactions on Systems Man and Cybernetics Part C (Applications and Reviews)
- URL/DOI: https://doi.org/10.1109/tsmcc.2007.913919
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 25. Self-improving reactive agents based on reinforcement learning, planning and teaching (1992)
- Authors: Long-Ji Lin
- Venue: Machine Learning
- URL/DOI: https://doi.org/10.1007/bf00992699
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 26. Reinforcement Learning and Dynamic Programming Using Function Approximators (2010)
- Authors: Lucian Buşoniu; Robert Babuška; Bart De Schutter; Damien Ernst
- Venue: 
- URL/DOI: https://doi.org/10.1201/9781439821091
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 27. Sim-to-Real Transfer of Robotic Control with Dynamics Randomization (2018)
- Authors: Xue Bin Peng; Marcin Andrychowicz; Wojciech Zaremba; Pieter Abbeel
- Venue: 
- URL/DOI: https://doi.org/10.1109/icra.2018.8460528
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization
- Hidden assumptions: training variation covers deployment mismatches
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 28. Position referencing and consistent world modeling for mobile robots (2005)
- Authors: Raja Chatila; Jean‐Paul Laumond
- Venue: 
- URL/DOI: https://doi.org/10.1109/robot.1985.1087373
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of using action-conditioned prediction as a robot world model.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 29. Finding Resonance: Adaptive Frequency Oscillators for Dynamic Legged Locomotion (2006)
- Authors: Jonas Buchli; Fumiya Iida; Auke Jan Ijspeert
- Venue: 
- URL/DOI: https://doi.org/10.1109/iros.2006.281802
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 30. ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation (2024)
- Authors: Xiaoqi Li; Mingxu Zhang; Yiran Geng; Haoran Geng; Yuxing Long; Yan Shen; Renrui Zhang; Jiaming Liu
- Venue: 
- URL/DOI: https://doi.org/10.1109/cvpr52733.2024.01710
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: object-centric state factorization; large generative/foundation model conditioning; contact/tactile dynamics modeling
- Hidden assumptions: objects and relations are separable and persist through contact; reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 31. Continuous control actions learning and adaptation for robotic manipulation through reinforcement learning (2022)
- Authors: Asad Ali Shahid; Dario Piga; Francesco Braghin; Loris Roveda
- Venue: Autonomous Robots
- URL/DOI: https://doi.org/10.1007/s10514-022-10034-z
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 32. Integrative Biomimetics of Autonomous Hexapedal Locomotion (2019)
- Authors: Volker Dürr; Paolo Arena; Holk Cruse; Chris J. Dallmann; Alin Drimus; Thierry Hoinville; Tammo Krause; Stefan Mátéfi‐Tempfli
- Venue: Frontiers in Neurorobotics
- URL/DOI: https://doi.org/10.3389/fnbot.2019.00088
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 33. Model Predictive Control With Environment Adaptation for Legged Locomotion (2021)
- Authors: Niraj Rathod; Angelo Bratta; Michele Focchi; Mario Zanon; Octavio Villarreal; Claudio Semini; Alberto Bemporad
- Venue: Institutional Research Information System (Università degli Studi di Trento)
- URL/DOI: http://hdl.handle.net/11572/330210
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 34. ChatGPT for Robotics: Design Principles and Model Abilities (2024)
- Authors: Sai Vemprala; Rogerio Bonatti; Arthur Bucker; Ashish Kapoor
- Venue: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2024.3387941
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 35. White paper - Agricultural Robotics: The Future of Robotic Agriculture (2018)
- Authors: Tom Duckett; Simon Pearson; Simon Blackmore; Bruce Grieve; Melvyn Smith
- Venue: UWE Research Repository (UWE Bristol)
- URL/DOI: https://openalex.org/W2885882173
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 36. Toward a New Generation of Electrically Controllable Hygromorphic Soft Actuators (2015)
- Authors: Silvia Taccola; Francesco Greco; Edoardo Sinibaldi; Alessio Mondini; Barbara Mazzolai; Virgilio Mattoli
- Venue: Advanced Materials
- URL/DOI: https://doi.org/10.1002/adma.201404772
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 37. Learning Neural Network Policies with Guided Policy Search under Unknown Dynamics (2014)
- Authors: Sergey Levine; Pieter Abbeel
- Venue: 
- URL/DOI: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.714.8044
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling; reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; model structure during deployment; downstream planner/controller response to model errors
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of broad learned dynamics/model-based robotics claims.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 38. Curiosity-Driven Exploration by Self-Supervised Prediction (2017)
- Authors: Deepak Pathak; Pulkit Agrawal; Alexei A. Efros; Trevor Darrell
- Venue: 
- URL/DOI: https://doi.org/10.1109/cvprw.2017.70
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 39. Optimization-Based Control for Dynamic Legged Robots (2023)
- Authors: Patrick M. Wensing; Michael Posa; Yue Hu; Adrien Escande; Nicolas Mansard; Andrea Del Prete
- Venue: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2023.3324580
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 40. Finite-Time Convergence Adaptive Fuzzy Control for Dual-Arm Robot With Unknown Kinematics and Dynamics (2018)
- Authors: Chenguang Yang; Yiming Jiang; Jing Na; Zhijun Li; Long Cheng; Chun‐Yi Su
- Venue: IEEE Transactions on Fuzzy Systems
- URL/DOI: https://doi.org/10.1109/tfuzz.2018.2864940
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 41. Whole-Body MPC and Online Gait Sequence Generation for Wheeled-Legged Robots (2021)
- Authors: Marko Bjelonic; Ruben Grandia; Oliver Harley; Cla Mattia Galliard; Samuel Zimmermann; Marco Hutter
- Venue: 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
- URL/DOI: https://doi.org/10.1109/iros51168.2021.9636371
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model; contact/tactile dynamics modeling
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 42. Counterfactual Multi-Agent Policy Gradients (2018)
- Authors: Jakob Foerster; Gregory Farquhar; Triantafyllos Afouras; Nantas Nardelli; Shimon Whiteson
- Venue: Proceedings of the AAAI Conference on Artificial Intelligence
- URL/DOI: https://doi.org/10.1609/aaai.v32i1.11794
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model; causal or counterfactual structure learning
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: which variables are repairable versus merely predicted
- Failure modes ignored: unobserved variables changing repair validity
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 43. Design Thinking for Social Innovation (2010)
- Authors: Tim Brown; Jocelyn Wyatt
- Venue: Development Outreach
- URL/DOI: https://doi.org/10.1596/1020-797x_12_1_29
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 44. Review of control strategies for robotic movement training after neurologic injury (2009)
- Authors: Laura Marchal–Crespo; David J. Reinkensmeyer
- Venue: Journal of NeuroEngineering and Rehabilitation
- URL/DOI: https://doi.org/10.1186/1743-0003-6-20
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 45. Artificial intelligence, machine learning and deep learning in advanced robotics, a review (2023)
- Authors: Mohsen Soori; Behrooz Arezoo; Roza Dastres
- Venue: Cognitive Robotics
- URL/DOI: https://doi.org/10.1016/j.cogr.2023.04.001
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 46. Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey (2020)
- Authors: Wenshuai Zhao; Jorge Pena Queralta; Tomi Westerlund
- Venue: 
- URL/DOI: https://doi.org/10.1109/ssci47803.2020.9308468
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: training variation covers deployment mismatches; reward feedback is the main signal for correcting model use
- Variables treated as fixed: downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 47. Model-based Reinforcement Learning: A Survey (2023)
- Authors: Thomas M. Moerland; Joost Broekens; Aske Plaat; Catholijn M. Jonker
- Venue: Foundations and Trends® in Machine Learning
- URL/DOI: https://doi.org/10.1561/2200000086
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model; uncertainty-aware model estimation
- Hidden assumptions: model errors remain tolerable over the planner horizon; epistemic uncertainty is calibrated enough to guide action; reward feedback is the main signal for correcting model use
- Variables treated as fixed: model structure during deployment
- Failure modes ignored: unobserved variables changing repair validity; planner exploitation of small model errors; miscalibrated confidence around rare failures
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 48. Robotics and Neuroscience (2014)
- Authors: Dario Floreano; Auke Jan Ijspeert; Stefan Schaal
- Venue: Current Biology
- URL/DOI: https://doi.org/10.1016/j.cub.2014.07.058
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 49. Reasons, Robots and the Extended Mind (2001)
- Authors: Andy Clark
- Venue: Mind & Language
- URL/DOI: https://doi.org/10.1111/1468-0017.00162
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 50. Online Hybrid Motion Planning for Dyadic Collaborative Manipulation via Bilevel Optimization (2020)
- Authors: Theodoros Stouraitis; Iordanis Chatzinikolaidis; Michael Gienger; Sethu Vijayakumar
- Venue: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2020.2992987
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: model errors remain tolerable over the planner horizon; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 51. Model-Based Approaches to Active Perception and Control (2017)
- Authors: Giovanni Pezzulo; Francesco Donnarumma; Pierpaolo Iodice; Domenico Maisto; Ivilin Peev Stoianov
- Venue: Entropy
- URL/DOI: https://doi.org/10.3390/e19060266
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 52. Feedback-error-learning neural network for trajectory control of a robotic manipulator (1988)
- Authors: Hiroyuki Miyamoto; Mitsuo Kawato; Tohru Setoyama; Ryoji Suzuki
- Venue: Neural Networks
- URL/DOI: https://doi.org/10.1016/0893-6080(88)90030-5
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 53. A soft thumb-sized vision-based sensor with accurate all-round force perception (2022)
- Authors: Huanbo Sun; Katherine J. Kuchenbecker; Georg Martius
- Venue: Nature Machine Intelligence
- URL/DOI: https://doi.org/10.1038/s42256-021-00439-3
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 54. Rehabilitation robots for the treatment of sensorimotor deficits: a neurophysiological perspective (2018)
- Authors: Roger Gassert; Volker Dietz
- Venue: Journal of NeuroEngineering and Rehabilitation
- URL/DOI: https://doi.org/10.1186/s12984-018-0383-x
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 55. Learning for a Robot: Deep Reinforcement Learning, Imitation Learning, Transfer Learning (2021)
- Authors: Jiang Hua; Liangcai Zeng; Gongfa Li; Zhaojie Ju
- Venue: Sensors
- URL/DOI: https://doi.org/10.3390/s21041278
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 56. Optimized Assistive Human–Robot Interaction Using Reinforcement Learning (2015)
- Authors: Hamidreza Modares; Isura Ranatunga; Frank L. Lewis; Dan O. Popa
- Venue: IEEE Transactions on Cybernetics
- URL/DOI: https://doi.org/10.1109/tcyb.2015.2412554
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 57. Dynamic movement primitives in robotics: A tutorial survey (2023)
- Authors: Matteo Saveriano; Fares J. Abu‐Dakka; Aljaž Kramberger; Luka Peternel
- Venue: The International Journal of Robotics Research
- URL/DOI: https://doi.org/10.1177/02783649231201196
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 58. Domain randomization for transferring deep neural networks from simulation to the real world (2017)
- Authors: Josh Tobin; Rachel Fong; Alex Ray; Jonas Schneider; Wojciech Zaremba; Pieter Abbeel
- Venue: 
- URL/DOI: https://doi.org/10.1109/iros.2017.8202133
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization
- Hidden assumptions: training variation covers deployment mismatches
- Variables treated as fixed: contact/friction regime; model structure during deployment
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 59. Cautious Model Predictive Control Using Gaussian Process Regression (2019)
- Authors: Lukas Hewing; Juraj Kabzan; Melanie N. Zeilinger
- Venue: IEEE Transactions on Control Systems Technology
- URL/DOI: https://doi.org/10.1109/tcst.2019.2949757
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model; residual correction on top of a nominal model; uncertainty-aware model estimation
- Hidden assumptions: model errors remain tolerable over the planner horizon; a smooth additive residual can absorb the important physical mismatch; epistemic uncertainty is calibrated enough to guide action
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: miscalibrated confidence around rare failures
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 60. Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots (2021)
- Authors: Zhongyu Li; Xuxin Cheng; Xue Bin Peng; Pieter Abbeel; Sergey Levine; Glen Berseth; Koushil Sreenath
- Venue: 
- URL/DOI: https://doi.org/10.1109/icra48506.2021.9560769
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: residual correction on top of a nominal model; simulation-to-real transfer or domain randomization; reinforcement-learning objective around a learned model
- Hidden assumptions: a smooth additive residual can absorb the important physical mismatch; training variation covers deployment mismatches; reward feedback is the main signal for correcting model use
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 61. Integrating planning and reacting in a heterogeneous asynchronous architecture for controlling real-world mobile robots (1992)
- Authors: Erann Gat
- Venue: National Conference on Artificial Intelligence
- URL/DOI: https://www.flownet.com/gat/papers/aaai92.pdf
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of using action-conditioned prediction as a robot world model.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 62. Adaptive Impedance Control of Human–Robot Cooperation Using Reinforcement Learning (2017)
- Authors: Zhijun Li; Junqiang Liu; Zhicong Huang; Yan Peng; Huayan Pu; Liang Ding
- Venue: IEEE Transactions on Industrial Electronics
- URL/DOI: https://doi.org/10.1109/tie.2017.2694391
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling; reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 63. Evolution of Adaptive Behaviour in Robots by Means of Darwinian Selection (2010)
- Authors: Dario Floreano; Laurent Keller
- Venue: PLoS Biology
- URL/DOI: https://doi.org/10.1371/journal.pbio.1000292
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 64. Adaptive, Fast Walking in a Biped Robot under Neuronal Control and Learning (2007)
- Authors: Poramate Manoonpong; Tao Geng; Tomas Kulvičius; Bernd Porr; Florentin Wörgötter
- Venue: PLoS Computational Biology
- URL/DOI: https://doi.org/10.1371/journal.pcbi.0030134
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 65. Learning-based nonlinear model predictive control to improve vision-based mobile robot path-tracking in challenging outdoor environments (2014)
- Authors: Chris J. Ostafew; Angela P. Schoellig; Timothy D. Barfoot
- Venue: 
- URL/DOI: https://doi.org/10.1109/icra.2014.6907444
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: planning by rolling out a learned or hybrid dynamics model
- Hidden assumptions: model errors remain tolerable over the planner horizon; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 66. A Framework for Push-Grasping in Clutter (2011)
- Authors: Mehmet R. Doğar; Siddhartha S Srinivasa
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2011.vii.009
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: uncertainty-aware model estimation
- Hidden assumptions: model errors remain tolerable over the planner horizon; epistemic uncertainty is calibrated enough to guide action; scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence; miscalibrated confidence around rare failures
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 67. Adaptive control for mobile robot using wavelet networks (2002)
- Authors: Celso de Sousa; Elder M. Hemerly; Roberto Kawakami Harrop Galvão
- Venue: IEEE Transactions on Systems Man and Cybernetics Part B (Cybernetics)
- URL/DOI: https://doi.org/10.1109/tsmcb.2002.1018768
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 68. Wearable Robots: Biomechatronic Exoskeletons (2008)
- Authors: José L. Pons
- Venue: 
- URL/DOI: http://www.loc.gov/catdir/enhancements/fy0826/2008007358-d.html
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 69. Adaptive representation of dynamics during learning of a motor task (1994)
- Authors: Reza Shadmehr; FA Mussa-Ivaldi
- Venue: Journal of Neuroscience
- URL/DOI: https://doi.org/10.1523/jneurosci.14-05-03208.1994
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: contact/tactile dynamics modeling; simulation-to-real transfer or domain randomization
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 70. High-Dimensional Continuous Control Using Generalized Advantage Estimation (2015)
- Authors: John Schulman; Philipp Moritz; Sergey Levine; Michael I. Jordan; Pieter Abbeel
- Venue: arXiv (Cornell University)
- URL/DOI: https://arxiv.org/abs/1506.02438
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 71. Movement Smoothness Changes during Stroke Recovery (2002)
- Authors: Brandon Rohrer; Susan E. Fasoli; Hermano Igo Krebs; Richard L. Hughes; Bruce T. Volpe; Walter R. Frontera; Joel Stein; Neville Hogan
- Venue: Journal of Neuroscience
- URL/DOI: https://doi.org/10.1523/jneurosci.22-18-08297.2002
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 72. Functional Stages in the Formation of Human Long-Term Motor Memory (1997)
- Authors: Reza Shadmehr; Thomas Brashers-Krug
- Venue: Journal of Neuroscience
- URL/DOI: https://doi.org/10.1523/jneurosci.17-01-00409.1997
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 73. Neural Correlates of Reach Errors (2005)
- Authors: Jörn Diedrichsen; Yasmin L. Hashambhoy; Tushar D. Rane; Reza Shadmehr
- Venue: Journal of Neuroscience
- URL/DOI: https://doi.org/10.1523/jneurosci.1874-05.2005
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 74. Deep visual foresight for planning robot motion (2017)
- Authors: Chelsea Finn; Sergey Levine
- Venue: 
- URL/DOI: https://doi.org/10.1109/icra.2017.7989324
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: action-conditioned visual prediction / visual foresight; reinforcement-learning objective around a learned model
- Hidden assumptions: better prediction loss implies better embodied decisions; model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of using action-conditioned prediction as a robot world model.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 75. Artificial Intelligence in Advanced Manufacturing: Current Status and Future Outlook (2020)
- Authors: Jorge Arinez; Qing Chang; Robert X. Gao; Chengying Xu; Jianjing Zhang
- Venue: Journal of Manufacturing Science and Engineering
- URL/DOI: https://doi.org/10.1115/1.4047855
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 76. Modelling and control of a large quadrotor robot (2010)
- Authors: Pauline Pounds; Robert Mahony; Peter Corke
- Venue: Control Engineering Practice
- URL/DOI: https://doi.org/10.1016/j.conengprac.2010.02.008
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 77. Language Conditioned Imitation Learning Over Unstructured Data (2021)
- Authors: Corey Lynch; Pierre Sermanet
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2021.xvii.047
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 78. Finite Element Modeling of Soft Fluidic Actuators: Overview and Recent Developments (2020)
- Authors: Matheus S. Xavier; Andrew J. Fleming; Yuen Kuan Yong
- Venue: Advanced Intelligent Systems
- URL/DOI: https://doi.org/10.1002/aisy.202000187
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 79. Learning Robotic Manipulation through Visual Planning and Acting (2019)
- Authors: Angelina Wang; Thanard Kurutach; Kara Liu; Pieter Abbeel; Aviv Tamar
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2019.xv.074
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: causal or counterfactual structure learning
- Hidden assumptions: model errors remain tolerable over the planner horizon
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; planner exploitation of small model errors
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 80. Emergence of Functional Hierarchy in a Multiple Timescale Neural Network Model: A Humanoid Robot Experiment (2008)
- Authors: Yuichi Yamashita; Jun Tani
- Venue: PLoS Computational Biology
- URL/DOI: https://doi.org/10.1371/journal.pcbi.1000220
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 81. Generic Neural Locomotion Control Framework for Legged Robots (2020)
- Authors: Mathias Thor; Tomas Kulvičius; Poramate Manoonpong
- Venue: IEEE Transactions on Neural Networks and Learning Systems
- URL/DOI: https://doi.org/10.1109/tnnls.2020.3016523
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 82. Gibson Env: Real-World Perception for Embodied Agents (2018)
- Authors: Fei Xia; Amir Zamir; Zhiyang He; Alexander F. Sax; Jitendra Malik; Silvio Savarese
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/1808.10654
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 83. Review of machine learning methods in soft robotics (2021)
- Authors: Daekyum Kim; Sang-Hun Kim; Taekyoung Kim; Brian Byunghyun Kang; Minhyuk Lee; Wookeun Park; Subyeong Ku; DongWook Kim
- Venue: PLoS ONE
- URL/DOI: https://doi.org/10.1371/journal.pone.0246102
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 84. Deep reinforcement learning for modeling human locomotion control in neuromechanical simulation (2020)
- Authors: Seungmoon Song; Łukasz Kidziński; Xue Bin Peng; Carmichael Ong; Jennifer L. Hicks; Sergey Levine; Christopher G. Atkeson; Scott L. Delp
- Venue: bioRxiv (Cold Spring Harbor Laboratory)
- URL/DOI: https://doi.org/10.1101/2020.08.11.246801
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: large generative/foundation model conditioning; reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 85. Soft robotics towards sustainable development goals and climate actions (2023)
- Authors: Goffredo Giordano; Saravana Prashanth Murali Babu; Barbara Mazzolai
- Venue: Frontiers in Robotics and AI
- URL/DOI: https://doi.org/10.3389/frobt.2023.1116005
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 86. A Survey of Machine Learning Approaches for Mobile Robot Control (2024)
- Authors: Monika Rybczak; Natalia Popowniak; Agnieszka Lazarowska
- Venue: Robotics
- URL/DOI: https://doi.org/10.3390/robotics13010012
- Problem claimed: Model robot-body/environment dynamics well enough for adaptive locomotion control.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use; scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 87. Iterative Residual Policy for Goal-Conditioned Dynamic Manipulation of Deformable Objects (2022)
- Authors: Cheng Chi; Benjamin Burchfiel; Eric Cousineau; Siyuan Feng; Shuran Song
- Venue: 
- URL/DOI: https://doi.org/10.15607/rss.2022.xviii.016
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: residual correction on top of a nominal model; reinforcement-learning objective around a learned model
- Hidden assumptions: a smooth additive residual can absorb the important physical mismatch; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 88. Leveraging Morphological Computation for Controlling Soft Robots: Learning from Nature to Control Soft Robots (2023)
- Authors: Helmut Häuser; Thrishantha Nanayakkara; Fulvio Forni
- Venue: IEEE Control Systems
- URL/DOI: https://doi.org/10.1109/mcs.2023.3253422
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 89. Hybrid hierarchical learning for solving complex sequential tasks using the robotic manipulation network ROMAN (2023)
- Authors: Eleftherios Triantafyllidis; Fernando Acero; Zhaocheng Liu; Zhibin Li
- Venue: Nature Machine Intelligence
- URL/DOI: https://doi.org/10.1038/s42256-023-00709-2
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: reinforcement-learning objective around a learned model; uncertainty-aware model estimation
- Hidden assumptions: epistemic uncertainty is calibrated enough to guide action; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence; miscalibrated confidence around rare failures
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 90. An Energy Tank-Based Interactive Control Architecture for Autonomous and Teleoperated Robotic Surgery (2015)
- Authors: Federica Ferraguti; Nicola Preda; Auralius Manurung; Marcello Bonfè; Olivier Lambercy; Roger Gassert; Riccardo Muradore; Paolo Fiorini
- Venue: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2015.2455791
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 91. Heterogeneous Multi-Robot Cooperation (1994)
- Authors: Lynne E. Parker
- Venue: DSpace@MIT (Massachusetts Institute of Technology)
- URL/DOI: http://hdl.handle.net/1721.1/7056
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 92. A review of collective robotic construction (2019)
- Authors: Kirstin Petersen; Nils Napp; Robert Stuart‐Smith; Daniela Rus; Mirko Kovač
- Venue: Science Robotics
- URL/DOI: https://doi.org/10.1126/scirobotics.aau8479
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 93. Inverse design of nonlinear mechanical metamaterials via video denoising diffusion models (2023)
- Authors: Jan-Hendrik Bastek; Dennis M. Kochmann
- Venue: Nature Machine Intelligence
- URL/DOI: https://doi.org/10.1038/s42256-023-00762-x
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: large generative/foundation model conditioning; contact/tactile dynamics modeling
- Hidden assumptions: scale transfers to local physical counterfactual repair
- Variables treated as fixed: contact/friction regime; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 94. Soft Actor-Critic Algorithms and Applications (2018)
- Authors: Tuomas Haarnoja; Aurick Zhou; Kristian Hartikainen; George Tucker; Sehoon Ha; Jie Tan; Vikash Kumar; Henry Zhu
- Venue: arXiv (Cornell University)
- URL/DOI: http://arxiv.org/abs/1812.05905
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: Whether visually plausible prediction errors are the right unit of correction for embodied decisions.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 95. CHOMP: Gradient optimization techniques for efficient motion planning (2009)
- Authors: Nathan Ratliff; Matt Zucker; J. Andrew Bagnell; Siddhartha S Srinivasa
- Venue: 
- URL/DOI: https://doi.org/10.1109/robot.2009.5152817
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: reinforcement-learning objective around a learned model
- Hidden assumptions: model errors remain tolerable over the planner horizon; reward feedback is the main signal for correcting model use
- Variables treated as fixed: contact/friction regime; model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 96. Soft Robotic Grippers for Biological Sampling on Deep Reefs (2016)
- Authors: Kevin C. Galloway; Kaitlyn P. Becker; Brennan Phillips; Jordan Kirby; Stephen Licht; Dan Tchernov; Robert J. Wood; David F. Gruber
- Venue: Soft Robotics
- URL/DOI: https://doi.org/10.1089/soro.2015.0019
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; model structure during deployment; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of broad learned dynamics/model-based robotics claims.
- What it leaves open: A mechanism that treats physical counterexamples as first-class repair operators rather than more training loss.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 97. Triboelectric nanogenerator sensors for soft robotics aiming at digital twin applications (2020)
- Authors: Tao Jin; Zhongda Sun; Long Li; Quan Zhang; Minglu Zhu; Zixuan Zhang; Guangjie Yuan; Tao Chen
- Venue: Nature Communications
- URL/DOI: https://doi.org/10.1038/s41467-020-19059-3
- Problem claimed: Model action-conditioned physical change for manipulation/contact robustly enough to support robot decisions.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: contact/friction regime; model structure during deployment; downstream planner/controller response to model errors; observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of broad learned dynamics/model-based robotics claims.
- What it leaves open: A mechanism that treats physical counterexamples as first-class repair operators rather than more training loss.
- Hostile reason: High-citation/high-relevance prior that constrains broad novelty claims.

## 98. Human-Like Adaptation of Force and Impedance in Stable and Unstable Interactions (2011)
- Authors: Chenguang Yang; Gowrishankar Ganesh; Sami Haddadin; Sven Parusel; Alin Albu‐Schäffer; Etienne Burdet
- Venue: IEEE Transactions on Robotics
- URL/DOI: https://doi.org/10.1109/tro.2011.2158251
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: contact/tactile dynamics modeling
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized contact/friction failures under action; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 99. Robust adaptive finite‐time parameter estimation and control for robotic systems (2014)
- Authors: Jing Na; Muhammad Nasiruddin Mahyuddin; Guido Herrmann; Xuemei Ren; Phil Barber
- Venue: International Journal of Robust and Nonlinear Control
- URL/DOI: https://doi.org/10.1002/rnc.3247
- Problem claimed: Use a learned or hybrid world/action model to improve planning or control.
- Actual mechanism introduced: task-specific learned dynamics, representation, or planning model
- Hidden assumptions: the selected training objective exposes the deployment-critical model errors
- Variables treated as fixed: observability of repair-relevant state
- Failure modes ignored: localized action failures, planner-induced counterexamples, and post-failure repair credit assignment
- What it makes less novel: Weakens novelty of any generic online adaptation or residual model-repair framing.
- What it leaves open: Whether repairs are selected by decision failures rather than global prediction fit, and whether repair locality is explicit.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.

## 100. Collaborative Multi-Robot Search and Rescue: Planning, Coordination, Perception, and Active Vision (2020)
- Authors: Jorge Peña Queralta; Jussi Taipalmaa; Bilge Can Pullinen; Victor Kathan Sarker; Tuan Nguyen Gia; Hannu Tenhunen; Moncef Gabbouj; Jenni Raitoharju
- Venue: IEEE Access
- URL/DOI: https://doi.org/10.1109/access.2020.3030190
- Problem claimed: Transfer a learned or simulated dynamics/action model from source conditions to deployment.
- Actual mechanism introduced: simulation-to-real transfer or domain randomization
- Hidden assumptions: model errors remain tolerable over the planner horizon; training variation covers deployment mismatches
- Variables treated as fixed: model structure during deployment; observability of repair-relevant state
- Failure modes ignored: planner exploitation of small model errors; out-of-distribution deployment mismatch; semantic priors overriding physical evidence
- What it makes less novel: Weakens novelty of planner-in-the-loop learned dynamics control.
- What it leaves open: How planner-exposed model counterexamples are converted into bounded, targeted world-model edits.
- Hostile reason: Directly competes with online model repair, learned dynamics, visual foresight, or planner-in-loop world models.
