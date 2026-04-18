***

# Interactive GBM Path Generator

### Overview
The Interactive Geometric Brownian Motion (GBM) Path Generator is a terminal-based quantitative tool designed to simulate and visualize a single, stochastic trajectory of an asset's price over one trading year. By taking live inputs for spot price, expected drift, and implied volatility, the engine calculates the daily tug-of-war between deterministic returns and random market chaos, rendering the final path via a Matplotlib UI.

### Features
* **Interactive Terminal UI:** Utilizes ANSI color codes to create a clean, responsive command-line interface for dynamic parameter input.
* **Pure Stochastic Engine:** Isolates the Geometric Brownian Motion formula—the foundational physics engine behind the Black-Scholes model—to demonstrate log-normal price distribution.
* **Visual Rendering:** Automatically generates a 2D line plot of the simulated reality, allowing users to physically see the impact of volatility clustering and drift.
* **Vectorized Array Pre-Rolling:** Uses `numpy.random.standard_normal` to pre-generate the standard normal variables ($Z$) for the entire year, optimizing the calculation loop.

### The Engineering Thesis
Before scaling up to massive Monte Carlo simulations with 10,000 parallel universes, a quantitative developer must understand the atomic unit of market movement: a single trading day. 

This engine isolates that atomic unit. By stepping through time day-by-day ($dt = 1/252$), it applies a deterministic drift ($\mu$) and a randomized volatility shock ($\sigma \cdot Z$) to the previous day's price. This proves the core theorem of quantitative finance: while returns are normally distributed, asset *prices* are log-normally distributed (they can go to infinity, but cannot drop below zero).

### Installation & Requirements
This engine requires two standard Python data science libraries.

```bash
# Install the required dependencies
pip install numpy matplotlib

# Clone the repository
git clone https://github.com/yourusername/GBM-Path-Generator.git
cd Geometric_Brownian_Motion
```

### Usage
Run the script natively in your terminal. You will be prompted to enter the asset's current market parameters. Once the calculations finish, a separate window will pop up displaying the mapped trajectory.

```bash
python gbm_single_path.py
```

### Sample Output Matrix
```text
Please Insert Spot Price : 150.00

Please Insert driftness of the asset (-1.0 to 1.0): 0.12

Please Insert Implied Vol (1.0 = 100 %) : 0.25

Assuming one trading year had past....
Generating a single GBM reality...
Start Price: $150.00
Final Price (Day 252): $184.32
```
*(A Matplotlib window will launch automatically to display the plotted array).*

***

