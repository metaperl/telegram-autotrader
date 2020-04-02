from pyrogram import Client

import pyrogramconf

with Client("my_account", pyrogramconf.api_id, pyrogramconf.api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")