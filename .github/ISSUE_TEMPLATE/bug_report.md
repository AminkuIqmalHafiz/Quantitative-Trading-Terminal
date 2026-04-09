---
name: Bug Report (Quantitative/Execution Error)
about: Report a mathematical anomaly, API failure, or code error in a pricing engine.
title: "[BUG] "
labels: bug, triage
assignees: ''

---

**Describe the Bug**
A clear and concise description of what the bug is. (e.g., "The Cost-of-Carry continuous compounding formula is outputting negative values when T < 0.1.")

**To Reproduce**
Steps to reproduce the behavior:
1. Engine/Script run: [e.g., `basis_arbitrage_scanner.py`]
2. Ticker/Asset tested: [e.g., 'SPY']
3. Market parameters used: [e.g., r = 0.05, q = 0.02, T = 0.5]
4. See error

**Expected Theoretical Value**
What *should* the mathematical output or execution signal have been based on the textbook formula?

**Screenshots / Console Output**
If applicable, paste the terminal output or traceback error here. 

**Environment:**
 - OS: [e.g., Windows, macOS, Ubuntu]
 - Python Version: [e.g., 3.10]
 - Library Versions: [e.g., yfinance 0.2.18, numpy 1.24]
