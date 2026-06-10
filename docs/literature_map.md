# Literature Map

## Field Box
Robot world models for embodied decision making: learned or hybrid action models used by robots for planning, control, manipulation, locomotion, sim-to-real transfer, tactile/contact reasoning, and foundation-model-mediated physical reasoning.

The working boundary excludes purely text-only agents and purely offline vision prediction unless the model is used, or explicitly proposed for use, in robot action selection.

## Coverage
- Landscape sweep: 1016 entries in `docs/related_work_matrix.csv`.
- Serious skim: top 300 cumulative entries by relevance/citation heuristic.
- Deep read: top 240 cumulative entries, consisting of the 100 hostile papers plus 140 additional high-relevance papers.
- Hostile prior-work set: top 100 entries.
- Per-paper extraction fields are stored in the CSV: problem claimed, mechanism, hidden assumptions, fixed variables, ignored failures, novelty constraints, and remaining opening.

## Year And Venue Shape
- Most common recent years: 2020: 109, 2021: 91, 2018: 88, 2023: 84, 2019: 84, 2022: 65, 2017: 64, 2016: 53, 2015: 36, 2014: 32, 2013: 29, 2010: 26.
- Most common venues/sources: unknown venue: 104, IEEE Access: 34, arXiv (Cornell University): 31, IEEE Transactions on Robotics: 21, Journal of Neuroscience: 20, Frontiers in Robotics and AI: 19, Nature Communications: 17, The International Journal of Robotics Research: 12, Autonomous Robots: 12, Frontiers in Neurorobotics: 11, Sensors: 11, PLoS ONE: 11.

## Mechanism Clusters
### learned dynamics + MPC
- Landscape count: 702; top-300 count: 161.
- Representative papers: DeepMPC: Learning Deep Latent Features for Model Predictive Control (2015); Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control (2018); OpenSim: Simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement (2018); A novel type of compliant and underactuated robotic hand for dexterous grasping (2015); Real-Time Neural MPC: Deep Learning Model Predictive Control for Quadrotors and Agile Robotic Platforms (2023); One-shot learning of manipulation skills with online dynamics adaptation and neural network priors (2016).
- Novelty pressure: Planning with learned dynamics is not new; the paper must change the update target and trigger distribution.

### contact / tactile dynamics
- Landscape count: 265; top-300 count: 131.
- Representative papers: Transfer from Simulation to Real World through Learning Deep Inverse Dynamics Model (2016); DeepMPC: Learning Deep Latent Features for Model Predictive Control (2015); Self-Supervised Sim-to-Real Adaptation for Visual Robotic Manipulation (2020); Preparing for the Unknown: Learning a Universal Policy with Online System Identification (2017); VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023); Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control (2018).
- Novelty pressure: Planning with learned dynamics is not new; the paper must change the update target and trigger distribution.

### sim-to-real transfer
- Landscape count: 185; top-300 count: 78.
- Representative papers: Transfer from Simulation to Real World through Learning Deep Inverse Dynamics Model (2016); DeepMPC: Learning Deep Latent Features for Model Predictive Control (2015); Self-Supervised Sim-to-Real Adaptation for Visual Robotic Manipulation (2020); Preparing for the Unknown: Learning a Universal Policy with Online System Identification (2017); VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023); OpenSim: Simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement (2018).
- Novelty pressure: Training-time coverage is not enough; the contribution must operate during deployment after unexpected mismatch.

### curiosity / active exploration
- Landscape count: 152; top-300 count: 51.
- Representative papers: OpenSim: Simulating musculoskeletal dynamics and neuromuscular control to study human and animal movement (2018); Developmental robotics, optimal artificial curiosity, creativity, music, and the fine arts (2006); Gaussian Processes for Data-Efficient Learning in Robotics and Control (2013); Self-improving reactive agents based on reinforcement learning, planning and teaching (1992); Reinforcement Learning and Dynamic Programming Using Function Approximators (2010); Sim-to-Real Transfer of Robotic Control with Dynamics Randomization (2018).
- Novelty pressure: This cluster constrains broad claims; keep the central claim narrowly about repair loops.

### object-centric / scene graphs
- Landscape count: 87; top-300 count: 14.
- Representative papers: Large-Area Soft e-Skin: The Challenges Beyond Sensor Designs (2019); ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation (2024); Design Thinking for Social Innovation (2010); Reasons, Robots and the Extended Mind (2001); Generic Neural Locomotion Control Framework for Legged Robots (2020); Physically Grounded Vision-Language Models for Robotic Manipulation (2024).
- Novelty pressure: This cluster constrains broad claims; keep the central claim narrowly about repair loops.

### movement primitives / skill models
- Landscape count: 83; top-300 count: 35.
- Representative papers: Self-Supervised Sim-to-Real Adaptation for Visual Robotic Manipulation (2020); Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control (2018); Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors (2012); One-shot learning of manipulation skills with online dynamics adaptation and neural network priors (2016); Curiosity-Driven Exploration by Self-Supervised Prediction (2017); Design Thinking for Social Innovation (2010).
- Novelty pressure: This cluster constrains broad claims; keep the central claim narrowly about repair loops.

### foundation / language-conditioned robotics
- Landscape count: 50; top-300 count: 17.
- Representative papers: VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023); ManipLLM: Embodied Multimodal Large Language Model for Object-Centric Robotic Manipulation (2024); Model-Based Approaches to Active Perception and Control (2017); Language Conditioned Imitation Learning Over Unstructured Data (2021); Deep reinforcement learning for modeling human locomotion control in neuromechanical simulation (2020); Inverse design of nonlinear mechanical metamaterials via video denoising diffusion models (2023).
- Novelty pressure: Language/foundation planning is not new; grounded repair must override semantic priors.

### uncertainty / ensembles
- Landscape count: 49; top-300 count: 19.
- Representative papers: Transfer from Simulation to Real World through Learning Deep Inverse Dynamics Model (2016); Gaussian Processes for Data-Efficient Learning in Robotics and Control (2013); Model-based Reinforcement Learning: A Survey (2023); Cautious Model Predictive Control Using Gaussian Process Regression (2019); A Framework for Push-Grasping in Clutter (2011); Hybrid hierarchical learning for solving complex sequential tasks using the robotic manipulation network ROMAN (2023).
- Novelty pressure: Adding uncertainty alone is weak; the repair should be triggered by embodied contradictions and planner dependency.

### residual correction
- Landscape count: 16; top-300 count: 8.
- Representative papers: Cautious Model Predictive Control Using Gaussian Process Regression (2019); Reinforcement Learning for Robust Parameterized Locomotion Control of Bipedal Robots (2021); Neural Correlates of Reach Errors (2005); Iterative Residual Policy for Goal-Conditioned Dynamic Manipulation of Deformable Objects (2022); Neuromuscular Controller Embedded in a Powered Ankle Exoskeleton: Effects on Gait, Clinical Features and Subjective Perspective of Incomplete Spinal Cord Injured Subjects (2020); Mapping a Suburb With a Single Camera Using a Biologically Inspired SLAM System (2008).
- Novelty pressure: Residual correction is crowded; discontinuous guarded patches need to be central and justified.

### visual foresight / video prediction
- Landscape count: 13; top-300 count: 12.
- Representative papers: Visual Foresight: Model-Based Deep Reinforcement Learning for Vision-Based Robotic Control (2018); VisuoSpatial Foresight for Multi-Step, Multi-Task Fabric Manipulation (2020); Improvisation through Physical Understanding: Using Novel Objects As Tools with Visual Foresight (2019); VisuoSpatial Foresight for Multi-Step, Multi-Task Fabric Manipulation (2020); VisuoSpatial Foresight for Physical Sequential Fabric Manipulation (2021); Deep visual foresight for planning robot motion (2017).
- Novelty pressure: Next-frame or future-image quality is heavily occupied; novelty must be about how failures rewrite planner-facing transitions.

### online system identification
- Landscape count: 8; top-300 count: 7.
- Representative papers: Preparing for the Unknown: Learning a Universal Policy with Online System Identification (2017); Sim-to-Real: Learning Agile Locomotion For Quadruped Robots (2018); One-shot learning of manipulation skills with online dynamics adaptation and neural network priors (2016); Online Hybrid Motion Planning for Dyadic Collaborative Manipulation via Bilevel Optimization (2020); Generic Neural Locomotion Control Framework for Legged Robots (2020); Rapid Locomotion via Reinforcement Learning (2022).
- Novelty pressure: Online adaptation is not new; novelty requires local structural repairs beyond global parameter estimation.

### other embodied model/control priors
- Landscape count: 2; top-300 count: 1.
- Representative papers: ROSPlan: Planning in the Robot Operating System (2015); Explicability of humanitarian AI: a matter of principles (2021).
- Novelty pressure: This cluster constrains broad claims; keep the central claim narrowly about repair loops.

## Cross-Cutting Pattern
The sweep repeatedly treats the world model as something that should become more predictive, more uncertain, more robustly pretrained, or more globally adapted. The less explored mechanism is the deployment-time loop in which a robot's failed action edits the specific transition relation that the planner will otherwise keep exploiting.

## Directional Consequence
A strong paper should not claim that online adaptation, residual dynamics, MPC, visual foresight, or uncertainty are new. It should instead make the planner-facing repair operation central: a failed embodied counterexample creates a scoped transition patch; future planning is obligated to respect the patch; and success is measured by preventing repeated exploitation, not by lowering average prediction loss.
