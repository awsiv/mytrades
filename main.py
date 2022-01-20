import os
import logging
import re

from binance import Client
from exchanges.cbinance import MyTrade

logger = logging.getLogger()
logger.setLevel(logging.INFO)

binance_api_key = os.environ.get('BINANCE_API_KEY')
binance_api_secret = os.environ.get('BINANCE_API_SECRET')

client = Client(binance_api_key, binance_api_secret)

# Read symbols in this format (BTCUSDT, ETHUSDT, etc) from a file
# Filter out empty lines and commented lines
raw = open('/app/symbols.txt','r')
symbols = [x for x in raw.read().split('\n') if x != '' and re.search("^(?!#|\s).*", x)]
raw.close()

# Stable coins
stable_coins = [ 'USDT', 'BUSD', 'USDC' ]

total_pl = {
    'USDT': 0.0,
    'BUSD': 0.0,
    'USDC': 0.0,
}
total_spent = {
    'USDT': 0.0,
    'BUSD': 0.0,
    'USDC': 0.0,
}
for symbol in symbols:
    trades = client.get_my_trades(symbol=symbol)

    total_cost = {
        'USDT': 0.0,
        'BUSD': 0.0,
        'USDC': 0.0,
    }
    total_holdings = 0.0

    for i in stable_coins:
        if re.search(i,symbol):
            unit = i
            mytrades = []
            for trade in trades:
                t = MyTrade(trade)
                mytrades.append(t)
                if unit == 'USDT':
                    total_trade_value_usdt = t.get_total_trade_value_usdt()
                    total_cost['USDT'] = total_cost['USDT'] + total_trade_value_usdt
                elif unit == 'BUSD':
                    total_trade_value_busd = t.get_total_trade_value_busd()
                    total_cost['BUSD'] = total_cost['BUSD'] + total_trade_value_busd
                elif unit == 'USDC':
                    total_trade_value_usdc = t.get_total_trade_value_usdc()
                    total_cost['USDC'] = total_cost['USDC'] + total_trade_value_usdc
                total_holdings = total_holdings + t.get_trade_qty()

            current_price = client.get_avg_price(symbol=symbol)
            current_holding_value = {
                'USDT': 0.0,
                'BUSD': 0.0,
                'USDC': 0.0, 
            }
            current_holding_value[unit] = total_holdings * float(current_price['price'])

            # DCA
            average_spent = sum(i.price for i in mytrades) / len(mytrades)

            print(f"--------------------{[t.symbol]}-------------------------")
            print(f"Current holding {t.symbol} : {total_holdings}")
            print(f"Total spent {unit}: {total_cost[unit]}")
            print(f"Avg price {unit}: {average_spent}")
            print(f"Current price {unit}: {float(current_price['price'])}")
            print(f"Current holding value {t.symbol} : {current_holding_value[unit]}")
            # total_cost value can be -negative if loss
            print(f"Profit/loss {t.symbol}: {current_holding_value[unit] + total_cost[unit]}")

    for i in stable_coins:
        total_spent[i] = total_spent[i] + total_cost[i]
        total_pl[i] = total_pl[i] + current_holding_value[i] + total_cost[i]

print(f"=============================================")
for i in stable_coins:
    if total_spent[i] != 0.0:
        print(f"Total Spent {i} {total_spent[i]}")
        print(f"Total Profit/loss {i} {total_pl[i]}")
print(f"=============================================")
