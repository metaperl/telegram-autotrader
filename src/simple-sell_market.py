

# import setpath
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

OP_BUY = 0
OP_SELL = 1
OP_BUYLIMIT = 2
OP_SELLLIMIT = 3
OP_BUYSTOP = 4
OP_SELLSTOP = 5

zmq = DWX_ZeroMQ_Connector()
my_trade = zmq._generate_default_order_dict()
my_trade['_type'] = OP_SELL
my_trade['_symbol'] = 'CHFJPY'
zmq._DWX_MTX_NEW_TRADE_(_order=my_trade)

resp = zmq._thread_data_output
print(f"response={resp}")
