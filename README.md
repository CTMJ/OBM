# OBM — Operator-Based Model for Influence Diffusion in Social Networks

Research code for the paper **"An Operator-Based Approach for Modeling Influence
Diffusion in Complex Social Networks"** (*Journal of Social Computing*, 2021).

The **Operator-Based Model (OBM)** models how influence spreads over a weighted,
directed social network, using an operator (heat-diffusion style) formulation whose
evolution is computed via a matrix-exponential kernel. The project also implements
the **GTS-Greedy** seed-selection algorithm for influence maximisation, and compares
the OBM against classical diffusion models.

## What's included

- **OBM** — the Operator-Based Model
- **Baselines** — Heat-Diffusion (HD), Independent Cascade (ICM), Linear Threshold (LTM), and a Real-Diffusion (RD) reference
- **Seed selection** — GTS-Greedy and comparison strategies (k-step, greedy, degree, random)
- Experiment drivers that reproduce the diffusion and influence-maximisation comparisons

## Structure

```
OBM/
├── main.py                 # entry point: runs the comparison experiments
├── DiffusionModels/
│   ├── Constants/          # parameters and data paths
│   ├── Factor/             # operator construction + matrix-exponential kernel
│   ├── Graphs/             # weighted-graph representation
│   ├── Models/             # OBM, HD, ICM, LTM
│   └── imp/                # seed-selection algorithms
├── DataExtrraction/        # loading & preprocessing the network data
├── Dataset/                # sample Twitter dataset
├── Test/                   # experiment drivers
└── TestResult/             # output figures
```

## Requirements

Python 3.8+ with `numpy`, `scipy`, `matplotlib`, `networkx`:

```bash
pip install numpy scipy matplotlib networkx
```

## Run

From the project root:

```bash
python main.py
```

Data paths are set in `DiffusionModels/Constants/constants.py`. The full run
computes matrix exponentials over the network, so it can take a while.

## Citation

This code accompanies the paper:

> C. Jiang, A. D'Arienzo, W. Li, S. Wu, Q. Bai.
> "An Operator-Based Approach for Modeling Influence Diffusion in Complex Social Networks."
> *Journal of Social Computing*, 2021, 2(2): 166–182.

Code implemented by **Chenting Jiang** (first author).
