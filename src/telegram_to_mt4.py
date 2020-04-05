"""
main script to react to trade in Telegram channel and send to MT4.
"""
import channel.olafemi
import mt4
import pyrogramconf
from pyrogram import Client

LOT_SIZE = 0.01
SIGNAL_CHANNEL = 'PAID Subscribers Clone'
SIGNAL_CHANNEL_PREFIX = SIGNAL_CHANNEL[:16]

app = Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash)

@app.on_message()
def my_handler(client, message):
    print(f"Message Received={message}")
    chatroom_name = message.chat.title

    if not chatroom_name or (SIGNAL_CHANNEL_PREFIX not in chatroom_name):
        print(f"Message is not in {SIGNAL_CHANNEL_PREFIX}. Not parsing message.")
        return

    result = channel.olafemi.parse(message.text)
    print(f"Parse result={result}")

    trade = mt4.MT4()
    trade.both_pending_orders(
        result['action'], LOT_SIZE, result['symbol'], result['entry'], result['stoploss'], result['takeprofit']
    )


print(f"Let's do this {SIGNAL_CHANNEL_PREFIX}")
app.run()
