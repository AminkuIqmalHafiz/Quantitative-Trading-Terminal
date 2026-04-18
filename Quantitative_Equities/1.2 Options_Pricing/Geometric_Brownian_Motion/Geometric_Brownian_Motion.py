import numpy as np
import matplotlib.pyplot as plt

RED = ' \033[31m'
GREEN = '\033[32m'
BOLD = '\033[1m'


def generate_single_gbm_path(S0, mu, sigma, days):
    """
    Generates one single reality of a stock's future path using GBM.
    """
    # 1. Set the time step (1 day out of 252 trading days in a year)
    dt = 1 / 252.0
    
    # 2. Create an empty array to hold the prices, starting with today's price
    prices = np.zeros(days + 1)
    prices[0] = S0
    
    # 3. Pre-roll all the random dice (Z) for the entire year
    Z = np.random.standard_normal(days)
    
    # 4. Loop through each day and apply the GBM formula
    for t in range(1, days + 1):
        # Calculate the steady upward pull
        drift = (mu - 0.5 * sigma**2) * dt
        
        # Calculate the violent daily shock
        shock = sigma * np.sqrt(dt) * Z[t-1]
        
        # Calculate tomorrow's price based on today's price
        prices[t] = prices[t-1] * np.exp(drift + shock)
        
    return prices

if __name__ == "__main__":
    # --- CONFIGURE YOUR MARKET PARAMETERS ---
    spot_price = float(input(f"{GREEN}{BOLD}Please Insert Spot Price : "))   
    driftness = float(input(f"\n{GREEN}{BOLD}Please Insert driftness of the asset (-1.0 to 1.0): "))   
    implied_vol = float(input(f"\n{GREEN}{BOLD}Please Insert Implied Vol (1.0 = 100 %) : "))
    print (f"\n{RED}{BOLD} Assuming one trading year had past....")       
    trading_days = 252      

    print(f"{RED}{BOLD} Generating a single GBM reality...")
    
    # Run the math
    simulated_path = generate_single_gbm_path(spot_price, driftness, implied_vol, trading_days)
    
    print(f"Start Price: ${simulated_path[0]:.2f}")
    print(f"Final Price (Day 252): ${simulated_path[-1]:.2f}")

    # --- RENDER THE VISUAL CHART ---
    plt.figure(figsize=(10, 6))
    plt.plot(simulated_path, color='blue', linewidth=1.5)
    plt.title("Geometric Brownian Motion: Single Path Simulation")
    plt.xlabel("Trading Days")
    plt.ylabel("Asset Price ($)")
    plt.grid(True, alpha=0.3)
    plt.show()