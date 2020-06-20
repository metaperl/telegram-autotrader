from dataclasses import dataclass

import pymt5adapter
from pymt5adapter.const import ORDER_FILLING
from pymt5adapter.order import Order
from pymt5adapter.symbol import Symbol


class MySymbol(Symbol):

    def pips(self, amount):
        return amount * 10 * self.point


@dataclass
class myMT5:

    # TODO:
    # place order based on current market price
    # if market price "worse" (less profitable than entry) or near entry price, then enter at market
    # if market price "better" (more profitable than entry) then enter with a STOP order
    # be sure to log logic
    # Alternatively, just enter both a STOP and LIMIT order
    # and enter a certain number of each

    def both_pending_orders(self, buy_or_sell, lots, symbol, entry, stop_loss, take_profit):
        """
        Enter both a LIMIT and STOP order for a symbol.

        This is done because the signals that I get could be above or below market price and the broker will
        only honor one or the other. So instead of me trying to figure out which one will fly, just send both!

        :param buy_or_sell: should be either 'buy' or 'sell'
        :param lots: e.g. 0.01
        :param symbol: e.g. EURUSD
        :param entry: entry price for buy/sell stop
        :param sl: price
        :param tp: price
        :return:
        """

        actions = {
            'buy': [Order.as_buy_stop, Order.as_buy_limit],
            'sell': [Order.as_sell_stop, Order.as_sell_limit]
        }

        for action in actions[buy_or_sell]:
            self.order(action, symbol, entry, lots, stop_loss, take_profit)

    def order(self, trade_method, symbol, price, sl, tp, lots=0.01):
        """

        :param trade_method: a classmethod from pymt5adapter.Order
        :param symbol: e.g. EURUSD
        :param price: entry price for buy/sell stop
        :param lots: e.g. 0.01
        :param sl: how many pips away from entry is the SL
        :param tp: how many pips away from entry is the TP
        :return:
        """

        order_dict = dict(
            symbol=MySymbol(symbol),
            volume=lots,
            price=price,
            stoplimit=price,
            sl=sl,
            tp=tp,
            type_filling=ORDER_FILLING.FOK
        )

        o = trade_method(**order_dict)
        o.send()


