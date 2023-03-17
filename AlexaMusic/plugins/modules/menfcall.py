from pyrogram import Client, filters
from AlexaMusic import app
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AlexaMusic.core.call import Alexa
from AlexaMusic.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError


@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Alexa, message.chat.id)
    try:
        async with assistant:
            await assistant.join_group_call(message.chat.id, stream_type=StreamType().pulse_stream)
            text = "🔔 الأعضاء المتواجدين في الكول :\n\n"
            participants = await assistant.get_participants(message.chat.id)
            k = 0
            for participant in participants:
                info = participant
                mut = "يتحدث 🗣" if not info.muted else "ساكت 🔕"
                user = await client.get_users(participant.user_id)
                k += 1
                text += f"{k}➤{user.mention}➤{mut}\n"
            text += f"\nعددهم : {len(participants)}\n✔️"
            await message.reply(text)
    except NoActiveGroupCall:
        await message.reply("عمووووو الكول مش مفتوح اصلااا\n❌")
    except TelegramServerError:
        await message.reply("ارسل الأمر مرة أخرى، حدثت مشكلة في
