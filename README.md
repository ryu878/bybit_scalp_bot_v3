# Bybit Scalp Bot v3 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://aadresearch.xyz) [![Generic badge](https://img.shields.io/badge/Python-3.8+-<COLOR>.svg)](https://aadresearch.xyz) 
Liquidation-Based Trading Bot (Shorts Only)

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Overview:
This project is a trading bot designed to leverage liquidation data to identify potential market opportunities and execute short trades. The bot focuses exclusively on short positions, but the architecture is modular, allowing you to easily extend it to support long positions if desired. The primary goal of this project is educational, providing a hands-on opportunity to learn about trading strategies, market data analysis, and algorithmic trading.

## Key Features
1. **Liquidation Data Integration:**
   - The bot monitors liquidation events in real-time using data from Bybit API.
   - It identifies large liquidation clusters, which often indicate potential market reversals or increased volatility.

2. **Short-Only Strategy:**
   - The bot is configured to open short positions when specific liquidation-based conditions are met (e.g., a surge in long liquidations suggesting potential downward pressure).

3. **Risk Management:**
   - Includes averaging and take-profit mechanisms to manage risk.
   - Position sizing is static and you can adjust it using settings.

4. **Modular Design:**
   - The code is structured to allow easy addition of long-position support.
   - Customizable parameters for strategy tuning.

5. **Educational Focus:**
   - The project is designed for learning purposes, with clear documentation and comments in the code.
   - Encourages experimentation with different strategies and parameters.


## How It Works
1. The bot continuously monitors liquidation data from the exchange.
2. When a significant liquidation event occurs (e.g., a large number of long positions liquidated), the bot evaluates market conditions.
3. If the conditions align with the strategy (e.g., overbought signals, bearish price action), the bot opens a short position.
4. The trade is managed according to predefined risk management rules.

## Future Enhancements (Optional)
- Add support for long positions to create a more balanced strategy.
- Incorporate machine learning models to predict liquidation patterns.
- Integrate additional data sources, such as funding rates or order book depth.
- Improve the backtesting framework with more advanced analytics.


## Disclaimer
This project is for educational purposes only. Trading involves significant risk, and you should never trade with money you cannot afford to lose. The strategy implemented in this bot may not be profitable, and past performance is not indicative of future results. Use at your own risk.

```
git clone git@github.com:ryu878/bybit_scalp_bot_v3.git

conda create --name BybitScalpBotv3 -c conda-forge python=3.11

conda activate BybitScalpBotv3

pip install -r requirements.txt
```
