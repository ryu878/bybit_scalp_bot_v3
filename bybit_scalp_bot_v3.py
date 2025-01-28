# Bybit Scalp Bot v3
# (C) 2025 Ryan Hayabusa 
# Github: https://github.com/ryu878 
# Discord: https://discord.gg/zSw58e9Uvf
# Join Bybit and receive up to $6,045 in Bonuses: https://www.bybit.com/invite?ref=P11NJW
# Web: https://aadresearch.xyz
#######################################################################################################
from _config import *
from pybit.unified_trading import HTTP
from pybit.exceptions import InvalidRequestError
import importlib
import json



# Create Bybit Client Session
session = HTTP(testnet=False, api_key=api_key, api_secret=api_secret)

# Dynamically Import the Strategy Module
try:
    strategy_module = importlib.import_module(strategy_name)
except ImportError:
    print(f' Module {strategy_name} not found')


# Get Balance Data
get_balance = session.get_wallet_balance(accountType=acc_type, coin=coin)
# print(get_balance)

# Convert data to JSON string
json_data = json.dumps(get_balance)
data = json.loads(json_data)

accountIMRate = data['result']['list'][0]['accountIMRate']
accountMMRate = data['result']['list'][0]['accountMMRate']
totalEquity = data['result']['list'][0]['totalEquity']
totalWalletBalance = data['result']['list'][0]['totalWalletBalance']
totalMarginBalance = data['result']['list'][0]['totalMarginBalance']
totalAvailableBalance = data['result']['list'][0]['totalAvailableBalance']
totalPerpUPL = data['result']['list'][0]['totalPerpUPL']
totalInitialMargin = data['result']['list'][0]['totalInitialMargin']
totalMaintenanceMargin = data['result']['list'][0]['totalMaintenanceMargin']

print(f' ╭─────────────────────────────────────────────╮')
print(f' │          Ryuryu\'s bybit bot v2.14           │')
print(f' ├─────────────────────────────────────────────┤')
print(f' │            Total Equity: {totalEquity}')
print(f' │    Total Wallet Balance: {totalWalletBalance}')
print(f' │    Total Margin Balance: {totalMarginBalance}')
print(f' │ Total Available Balance: {totalAvailableBalance}')


symbol = input('What Asset To trade? ')
symbol = (symbol+'USDT').upper()

lot_size = input('Lot size? ')
if '.' in str(lot_size):
        lot_size = float(lot_size)
else:
    lot_size = int(lot_size)