# Alexa

from AlexaMusic import app
from pyrogram import filters
from strings.filters import command


@app.on_message(
    command("ايدي")
)
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ايديهك**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ايدي**: `{reply.from_user.id}`\n**ايدي المجموعة**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ايديهك**: `{message.from_user.id}`\n**ايدي المجموعة**: `{message.chat.id}`"
        )
