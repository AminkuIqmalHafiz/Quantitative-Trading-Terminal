***

# Institutional BSM Pricing Engine

### Overview
The BSM Pricing Engine is a high-speed, zero-dependency Python terminal application designed to calculate the theoretical fair value of European Call and Put options. Utilizing the Black-Scholes-Merton mathematical framework, it processes real-time market parameters (Spot, Strike, DTE, Volatility, Risk-Free Rate, and Dividend Yield) to output precise derivative valuations.

### Features
* **Zero-Dependency Architecture:** Built entirely on Python's standard `math` and `os` libraries. It requires no heavy external packages (like `scipy` or `numpy`), making it incredibly lightweight and perfect for embedding inside larger, high-frequency trading systems.
* **Merton Extension:** Natively supports continuous dividend yield ($q$) integrations, allowing for the accurate pricing of options on dividend-paying equities and indices.
* **Custom CDF Engine:** Bypasses standard statistical libraries by hardcoding the Cumulative Distribution Function (CDF) utilizing the Gauss error function (`math.erf`), maximizing execution speed.
* **Clean Terminal UI:** Utilizes dynamic console clearing and ANSI color formatting for a distraction-free, institutional risk-desk interface.

### The Engineering Thesis
At the core of every quantitative derivatives desk sits the Black-Scholes model. It is the mathematical abstraction of market chaos, utilizing geometric Brownian motion to model the random walk of asset prices. 

While retail traders look at the "price" of an option, institutional systems look at the probability of that option expiring In-The-Money (represented by $d1$ and $d2$), weighted by implied volatility ($\sigma$) and discounted to present value ($r$). This engine strips away bloated UI layers and executes that exact mathematical probability with absolute precision.

### Installation & Requirements
This engine is built entirely on Python's standard library. No `pip install` commands are required.

```bash
# Clone the repository
git clone https://github.com/yourusername/BSM-Pricing-Engine.git

# Navigate to the directory
cd BSM-Pricing-Engine
```

### Usage
Run the script natively in your terminal. You will be prompted to enter the current market parameters for the option you wish to price.

```bash
python Black_Scholes_Model.py
```

### Sample Output Matrix
```text
=== INSTITUTIONAL BSM PRICING ENGINE ===

[*] Awaiting Market Parameters...
Enter Spot Price ($): 450.00
Enter Strike Price ($): 455.00
Enter Days to Expiration (DTE): 30
Enter Risk-Free Rate (e.g., 0.05 for 5%): 0.0525
Enter Implied Volatility (e.g., 0.20 for 20%): 0.18
Enter Dividend Yield (e.g., 0.02 for 2%, or 0 if none): 0.015

--- THEORETICAL FAIR VALUE ---
European Call Option: $6.02
European Put Option:  $9.71
```