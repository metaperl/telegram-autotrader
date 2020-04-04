from dataclasses import dataclass, field
from typing import Any

import pips
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

OP_BUY = 0
OP_SELL = 1
OP_BUY_LIMIT = 2
OP_SELL_LIMIT = 3
OP_BUY_STOP = 4
OP_SELL_STOP = 5


@dataclass
class MT4:
    zmq: Any = field(default_factory=DWX_ZeroMQ_Connector)

    # TODO:
    # place order based on current market price
    # if market price "worse" (less profitable than entry) or near entry price, then enter at market
    # if market price "better" (more profitable than entry) then enter with a STOP order
    # be sure to log logic
    # Alternatively, just enter both a STOP and LIMIT order
    # and enter a certain number of each

    def both_pending_orders(self, trade_type, lots, symbol, entry, stop_loss, take_profit):
        """
        Enter both a LIMIT and STOP order for a symbol.

        This is done because the signals that I get could be above or below market price and the broker will
        only honor one or the other. So instead of me trying to figure out which one will fly, just send both!

        :param trade_type: should be either 'buy' or 'sell'
        :param lots: e.g. 0.01
        :param symbol: e.g. EURUSD
        :param entry: entry price for buy/sell stop
        :param sl: price
        :param tp: price
        :return:
        """

        actions = {
            'buy': [OP_BUY_LIMIT, OP_BUY_STOP],
            'sell': [OP_SELL_LIMIT, OP_SELL_STOP]
        }

        stop_loss_pips = pips.pips_between(entry, stop_loss)
        take_profit_pips = pips.pips_between(entry, take_profit)

        for action in actions[trade_type]:
            self.order(action, symbol, entry, stop_loss_pips, take_profit_pips)

    def order(self, trade_type, symbol, price, lots=0.01, sl=170, tp=20):
        """

        :param trade_type: should be either OP_BUY_STOP or OP_BUY_LIMIT
        :param symbol: e.g. EURUSD
        :param price: entry price for buy/sell stop
        :param lots: e.g. 0.01
        :param sl: how many pips away from entry is the SL
        :param tp: how many pips away from entry is the TP
        :return:
        """
        sl = self.pips_to_points(sl)
        tp = self.pips_to_points(tp)

        my_trade = self.zmq._generate_default_order_dict()
        my_trade['_type'] = trade_type
        my_trade['_symbol'] = symbol
        my_trade['_SL'] = sl
        my_trade['_TP'] = tp
        my_trade['_lots'] = lots
        self.zmq._DWX_MTX_NEW_TRADE_(_order=my_trade)
