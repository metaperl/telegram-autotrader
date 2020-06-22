from pymt5adapter.symbol import Symbol
import pymt5adapter

class MySymbol(Symbol):
    pass


with pymt5adapter.connected(enable_real_trading=True, debug_logging=True):

    symbol_str = 'AUDUSD'

    print(f"{symbol_str}")
    s = MySymbol(symbol_str)
    print("hi there")
    print(s, type(s))
    