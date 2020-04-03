

import setpath
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

OP_BUY = 0
OP_SELL = 1
OP_BUY_LIMIT = 2
OP_SELL_LIMIT = 3
OP_BUY_STOP = 4
OP_SELL_STOP = 5

zmq = DWX_ZeroMQ_Connector()
my_trade = zmq._generate_default_order_dict()
my_trade['_type'] = OP_SELL_LIMIT
my_trade['_symbol'] = 'EURCHF'
my_trade['_price'] = 1.06
zmq._DWX_MTX_NEW_TRADE_(_order=my_trade)

resp = zmq._thread_data_output
print(f"response={resp}")