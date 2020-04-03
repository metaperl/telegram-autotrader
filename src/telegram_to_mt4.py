"""
main script to react to trade in Telegram channel and send to MT4.
"""

import setpath
from pyrogram import Client
import mt4
import pyrogramconf
import re


app = Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash)

SIGNAL_CHANNEL = 'PAID Subscribers Clone'
SIGNAL_CHANNEL_PREFIX = SIGNAL_CHANNEL[:16]
@app.on_message()
def my_handler(client, message):
    print(f"Message Received={message}")

    chatroom_name = message.chat.title
    print(f"Chatroom title={chatroom_name}")

    if not chatroom_name or (SIGNAL_CHANNEL_PREFIX not in chatroom_name):
        print(f"Message is not in {SIGNAL_CHANNEL_PREFIX}. Not parsing message.")
        return

    # match #SYS Coin at #Bittrex
    re1 = re.compile(
        r'#(\S+)\s+at\s+({})'.format(self.exchange_label),
        re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    m = re1.search(message)
    if m:
        coin, exchange = m.groups()
        return coin, exchange

print(f"Let's do this {SIGNAL_CHANNEL_PREFIX}")
app.run()

