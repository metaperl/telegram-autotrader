"""
main script to react to trade in Telegram channel and send to MT4.
"""

from pyrogram import Client
import mt4
import pyrogramconf
import re


app = Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash)

SIGNAL_CHANNEL = 'PAID Subscribers Clone'

@app.on_message()
def my_handler(client, message):
    print(f"Message Received={message}")

    chatroom_name = message.chat.title
    if chatroom_name != SIGNAL_CHANNEL:
        print(f"Message is not from {SIGNAL_CHANNEL}. Not parsing message.")
        return

    print(f"Chatroom title={message.chat.title}")
    # match #SYS Coin at #Bittrex
    re1 = re.compile(
        r'#(\S+)\s+at\s+({})'.format(self.exchange_label),
        re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    m = re1.search(message)
    if m:
        coin, exchange = m.groups()
        return coin, exchange


app.run()

