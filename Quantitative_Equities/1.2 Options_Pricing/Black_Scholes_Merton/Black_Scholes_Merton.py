import math

# --- ANSI COLOR CODES ---
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[31m'

def norm_cdf(x):
    """
    Calculates the Cumulative Distribution Function (CDF) for a standard normal distribution.
    This replaces the need to import scipy.stats.norm.
    """
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def black_scholes_merton(S, K, T, r, sigma, q=0.0):
    """
    Calculates the theoretical fair value of European Call and Put options.
    
    S     : Spot price of the underlying asset
    K     : Strike price of the option
    T     : Time to expiration in years (Days to Expiration / 365)
    r     : Risk-free interest rate (e.g., 0.05 for 5%)
    sigma : Implied volatility of the underlying asset (e.g., 0.20 for 20%)
    q     : Continuous dividend yield (default is 0.0)
    """
    # Prevent division by zero if the option expires today
    if T <= 0:
        return max(0.0, S - K), max(0.0, K - S)

    # The Core BSM Mathematical Engine
    d1 = (math.log(S / K) + (r - q + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))

    # Pricing the Call and Put
    call_price = (S * math.exp(-q * T) * norm_cdf(d1)) - (K * math.exp(-r * T) * norm_cdf(d2))
    put_price = (K * math.exp(-r * T) * norm_cdf(-d2)) - (S * math.exp(-q * T) * norm_cdf(-d1))

    return call_price, put_price

def run_bsm_terminal():
    
    print(f"{BOLD}{CYAN}=== BSM PRICING==={RESET}\n")

    print(f"{YELLOW}[*] Awaiting Market Parameters...{RESET}")
    # Wrapped correctly with float() exactly as we patched earlier today!
    S = float(input("Enter Spot Price ($): "))
    K = float(input("Enter Strike Price ($): "))
    dte = float(input("Enter Days to Expiration (DTE): "))
    r = float(input("Enter Risk-Free Rate (e.g., 0.05 for 5%): "))
    sigma = float(input("Enter Implied Volatility (e.g., 0.20 for 20%): "))
    q = float(input("Enter Dividend Yield (e.g., 0.02 for 2%, or 0 if none): "))

    # Convert DTE to Years for the mathematical formula
    T = dte / 365.0 

    # Execute the engine
    call_val, put_val = black_scholes_merton(S, K, T, r, sigma, q)

    print(f"\n{BOLD}{CYAN}--- THEORETICAL FAIR VALUE ---{RESET}")
    print(f"European Call Option: {BOLD}{GREEN}${call_val:.2f}{RESET}")
    print(f"European Put Option:  {BOLD}{GREEN}${put_val:.2f}{RESET}\n")

if __name__ == "__main__":
    while True :
        run_bsm_terminal()
        again = input(f"{BOLD}Want to try again? (Y/N): ")
        if again == "y" or again == "Y":
            continue
        elif again == "n" or again =="N":
            print (f"{BOLD}{RED}Initiating exit code. Exiting....")
            break
    

