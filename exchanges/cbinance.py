import logging
from typing import List

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class MyTrade:
    def __init__(self, trade):
        self.symbol = str(trade['symbol'])
        self.id = trade['id']
        self.orderId = trade['orderId']
        self.orderListId = trade['orderListId']
        self.price = float(trade['price'])
        self.qty = float(trade['qty'])
        self.quoteQty = float(trade['quoteQty'])
        self.commission = float(trade['commission'])
        self.commissionAsset = trade['commissionAsset']
        self.time = trade['time']
        self.isBuyer = bool(trade['isBuyer'])
        self.isMaker = trade['isMaker']
        self.isBestMatch = trade['isBestMatch']

        logging.debug(trade)

        self.trade_value_usdt = self.price * self.qty
        self.trade_charge_usdt = self.price * self.commission
        self.trade_value_busd = self.price * self.qty
        self.trade_charge_busd = self.price * self.commission
        self.trade_value_usdc = self.price * self.qty
        self.trade_charge_usdc = self.price * self.commission

        if self.isBuyer is True:
            logging.debug(f"Bought {self.qty}{[self.symbol]} for {self.trade_value_usdt}UDST at {self.price}")
            self.total_trade_value_usdt = -self.trade_value_usdt - self.trade_charge_usdt
            logging.debug(f"Bought {self.qty}{[self.symbol]} for {self.trade_value_busd}BUSD at {self.price}")
            self.total_trade_value_busd = -self.trade_value_busd - self.trade_charge_busd
            logging.debug(f"Bought {self.qty}{[self.symbol]} for {self.trade_value_usdc}USDC at {self.price}")
            self.total_trade_value_usdc = -self.trade_value_usdc - self.trade_charge_usdc
        else:
            logging.debug(f"Sold {self.qty}{[self.symbol]} for {self.trade_value_usdt}USDT at {self.price}")
            self.total_trade_value_usdt = self.trade_value_usdt + self.trade_charge_usdt
            logging.debug(f"Sold {self.qty}{[self.symbol]} for {self.trade_value_busd}BUSD at {self.price}")
            self.total_trade_value_busd = self.trade_value_busd + self.trade_charge_busd
            logging.debug(f"Sold {self.qty}{[self.symbol]} for {self.trade_value_usdc}USDC at {self.price}")
            self.total_trade_value_usdc = self.trade_value_usdc + self.trade_charge_usdc

        logging.debug(f"{[self.symbol]} trade charge: {self.trade_charge_usdt}")
        logging.debug(f"{[self.symbol]} total trade including charges: {self.total_trade_value_usdt}")
        logging.debug(f"{[self.symbol]} trade charge: {self.trade_charge_busd}")
        logging.debug(f"{[self.symbol]} total trade including charges: {self.total_trade_value_busd}")
        logging.debug(f"{[self.symbol]} trade charge: {self.trade_charge_usdc}")
        logging.debug(f"{[self.symbol]} total trade including charges: {self.total_trade_value_usdc}")

    def get_trade_charge_usdt(self):
        return self.trade_charge_usdt

    def get_trade_charge_busd(self):
        return self.trade_charge_busd

    def get_trade_charge_usdc(self):
        return self.trade_charge_usdc

    def get_total_trade_value_usdt(self):
        return self.total_trade_value_usdt

    def get_total_trade_value_busd(self):
        return self.total_trade_value_busd

    def get_total_trade_value_usdc(self):
        return self.total_trade_value_usdc

    def get_trade_qty(self):
        if self.isBuyer:
            return self.qty
        else:
            return -self.qty


# {'symbol': 'GRTUSDT',
#  'id': 70298192,
#  'orderId': 727304680,
#  'orderListId': -1,
#  'price': '0.65000000',
#  'qty': '139.00000000',
#  'quoteQty': '90.35000000',
#  'commission': '0.13900000',
#  'commissionAsset': 'GRT',
#  'time': 1641274543982,
#  'isBuyer': True,
#  'isMaker': True,
#  'isBestMatch': True
# }


# symbol info:
# {
# 'symbol': 'GRTUSDT',
# 'status': 'TRADING',
# 'baseAsset': 'GRT',
# 'baseAssetPrecision': 8,
# 'quoteAsset': 'USDT',
# 'quotePrecision': 8,
# 'quoteAssetPrecision': 8,
# 'baseCommissionPrecision': 8,
# 'quoteCommissionPrecision': 8,
# 'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT'],
# 'icebergAllowed': True,
# 'ocoAllowed': True, 'quoteOrderQtyMarketAllowed': True, 'isSpotTradingAllowed': True,
# 'isMarginTradingAllowed': True,
# 'filters': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00010000', 'maxPrice': '1000.00000000', 'tickSize': '0.00010000'},
# {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5},
# {'filterType': 'LOT_SIZE', 'minQty': '1.00000000', 'maxQty': '900000.00000000', 'stepSize': '1.00000000'},
# {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5},
# {'filterType': 'ICEBERG_PARTS', 'limit': 10},
# {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '1565586.65809589', 'stepSize': '0.00000000'},
# {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200},
# {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}],
# 'permissions': ['SPOT', 'MARGIN']}
