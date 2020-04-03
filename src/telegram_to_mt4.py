"""
main script to react to trade in Telegram channel and send to MT4.
"""

from pyrogram import Client
import mt4
import pyrogramconf


app = Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash)


@app.on_message()
def my_handler(client, message):
    print(f"Message Received={message}")

app.run()

