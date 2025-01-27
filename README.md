# Bybit Scalp Bot v3 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://aadresearch.xyz) [![Generic badge](https://img.shields.io/badge/Python-3.8+-<COLOR>.svg)](https://aadresearch.xyz) 
Liquidation-Based Trading Bot (Shorts Only)

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Overview:
This project is a trading bot designed to leverage liquidation data to identify potential market opportunities and execute short trades. The bot focuses exclusively on short positions, but the architecture is modular, allowing you to easily extend it to support long positions if desired. The primary goal of this project is educational, providing a hands-on opportunity to learn about trading strategies, market data analysis, and algorithmic trading.

## Key Features
1. **Liquidation Data Integration:**
   - The bot monitors liquidation events in real-time using data from exchanges or APIs that provide liquidation feeds.
   - It identifies large liquidation clusters, which often indicate potential market reversals or increased volatility.

2. **Short-Only Strategy:**
   - The bot is configured to open short positions when specific liquidation-based conditions are met (e.g., a surge in long liquidations suggesting potential downward pressure).
   - It uses technical indicators (e.g., RSI, moving averages) or price action to confirm entry points.

3. **Risk Management:**
   - Includes stop-loss and take-profit mechanisms to manage risk.
   - Position sizing is dynamic, based on account balance and risk tolerance.

4. **Modular Design:**
   - The code is structured to allow easy addition of long-position support.
   - Customizable parameters for strategy tuning (e.g., liquidation threshold, confirmation indicators).

5. **Real-Time Trading:**
   - Connects to supported exchanges via API to execute trades in real-time.
   - Logs all trades and performance metrics for review.

6. **Educational Focus:**
   - The project is designed for learning purposes, with clear documentation and comments in the code.
   - Encourages experimentation with different strategies and parameters.


```
conda create --name BybitScalpBotv3 -c conda-forge python=3.11

conda activate BybitScalpBotv3

pip install -r requirements.txt
```
