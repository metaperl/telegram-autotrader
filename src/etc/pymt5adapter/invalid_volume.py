import MetaTrader5 as mt5
import pymt5adapter
from pymt5adapter.order import Order
from pymt5adapter.symbol import Symbol


LOT=1.118237 # to force error

class MySymbol(Symbol):

    def pips(self, amount):
        return amount * 10 * self.point

def buy_stop():
    symbol_str = 'EURUSD'
    symbol = MySymbol(symbol_str)

    entry = symbol.ask + symbol.pips(50)
    print(f"Entry {entry}")
    sl = entry - symbol.pips(10)
    tp = entry + symbol.pips(10)

    deviation = 20

    o = Order.as_buy_stop(symbol=symbol, volume=LOT, price=entry, stoplimit=entry, sl=sl, tp=tp,
                          deviation=deviation, type_filling=mt5.ORDER_FILLING_FOK)

    r = o.send()
    print(r)


def buy_limit():
    symbol_str = 'EURUSD'
    symbol = MySymbol(symbol_str)

    entry = symbol.ask - symbol.pips(50)
    print(f"Entry {entry}")
    sl = entry - symbol.pips(10)
    tp = entry + symbol.pips(10)

    deviation = 20

    o = Order.as_buy_limit(symbol=symbol, volume=LOT, price=entry, stoplimit=entry, sl=sl, tp=tp,
                          deviation=deviation, type_filling=mt5.ORDER_FILLING_FOK)

    r = o.send()
    print(r)


if __name__ == '__main__':
    with pymt5adapter.connected(enable_real_trading=True):
        buy_stop()
        buy_limit()
