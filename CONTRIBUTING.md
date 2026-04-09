# Contributing to Aminku Financial Engineering

First off, thank you for considering contributing to this repository. This project aims to build institutional-grade quantitative pricing models and market infrastructure tools.

## The Engineering Standard
Because this repository deals with financial mathematics and theoretical pricing, strict adherence to quantitative accuracy and code cleanliness is required.

### 1. Adding a New Model
When submitting a new quantitative model (e.g., a new options pricer or risk scanner):
* **Mathematical Proof:** You must document the underlying mathematical framework (e.g., Black-Scholes, Cost-of-Carry, Monte Carlo) in the directory's `README.md`.
* **Standardized Libraries:** Rely heavily on `numpy`, `pandas`, and `scipy` for heavy mathematical lifting. Avoid unnecessary external dependencies.
* **Modularity:** Separate your data ingestion logic from your pure math functions. 

### 2. Code Style
* Use clear, descriptive variable names. In mathematical functions, standard financial notation is acceptable (e.g., `S0` for spot price, `r` for risk-free rate, `sigma` for volatility) provided it is commented.
* Include docstrings for all primary pricing functions explaining the inputs, outputs, and the theoretical model being applied.

### 3. Pull Request Process
1. Fork the repo and create your branch from `main`.
2. Ensure your code executes without errors and handles basic edge cases (e.g., division by zero, negative time to expiration).
3. Update the `README.md` in the relevant sub-directory with details of your new engine.
4. Submit the PR with a clear description of the model's purpose and any institutional concepts it applies.

## Reporting Bugs
If you find a mathematical error in a pricing engine or a breakdown in a scanner, please open an Issue using the provided Bug Report template, detailing the expected theoretical value versus the script's output.
