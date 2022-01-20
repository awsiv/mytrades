import os
import logging

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

total_pl = 0.0
total_spent = 0.0
for symbol in symbols:
    trades = client.get_my_trades(symbol=symbol)

    total_cost_usdt = 0.0
    total_holdings = 0.0

    for i in stable_coins:
        if re.search(i,symbol):
            unit = i
            mytrades = []
            for trade in trades:
                t = MyTrade(trade)
                mytrades.append(t)

                total_trade_value_usdt = t.get_total_trade_value_usdt()
                total_cost_usdt = total_cost_usdt + total_trade_value_usdt

                total_holdings = total_holdings + t.get_trade_qty()


            current_price = client.get_avg_price(symbol=symbol)
            current_holding_value_usdt = total_holdings * float(current_price['price'])

            # DCA
            average_spent = sum(i.price for i in mytrades) / len(mytrades)

            print(f"--------------------{[t.symbol]}-------------------------")
            print(f"Current holding {t.symbol} : {total_holdings}")
            print(f"Total spent {unit}: {total_cost_usdt}")
            print(f"Avg price {unit}: {average_spent}")
            print(f"Current price {unit}: {float(current_price['price'])}")
            print(f"Current holding value {t.symbol} : {current_holding_value_usdt}")
            print(f"Profit/loss {t.symbol}: {current_holding_value_usdt + total_cost_usdt}")  # total_cost_usdt can be -negative if loss
    total_spent = total_spent + total_cost_usdt
    total_pl = total_pl + current_holding_value_usdt + total_cost_usdt

print(f"=============================================")
print(f"Total Spent {total_spent}")
print(f"Total Profit/loss {total_pl}")
print(f"=============================================")
