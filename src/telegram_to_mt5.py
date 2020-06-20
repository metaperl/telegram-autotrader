"""
main script to react to trade in Telegram channel and send to MT5.
"""
import channel.olafemi
import myMT5
import pyrogramconf
from pyrogram import Client
import pymt5adapter

LOT_SIZE = 0.02
SIGNAL_CHANNEL = 'PAID: OpgtsFxSignals Clone'
SIGNAL_CHANNEL_PREFIX = SIGNAL_CHANNEL[:16]

app = Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash)

@app.on_message()
def my_handler(client, message):
    chatroom_name = message.chat.title

    if not chatroom_name or (SIGNAL_CHANNEL_PREFIX not in chatroom_name):
        # print(f"Message is not in {SIGNAL_CHANNEL_PREFIX}. Not parsing message.")
        return

    print(f"Relevant Message Received={message}")

    result = channel.olafemi.parse(message.text)
    print(f"Parse result={result}")

    with pymt5adapter.connected(enable_real_trading=True, debug_logging=True):
        trade = myMT5.myMT5()
        trade.both_pending_orders(
            result['action'], LOT_SIZE, result['symbol'], result['entry'], result['stoploss'], result['takeprofit']
        )


print(f"Let's do this {SIGNAL_CHANNEL_PREFIX}")
app.run()
