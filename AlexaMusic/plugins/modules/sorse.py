
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlexaMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlexaMusic import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "افاتار"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/aa84897eb42d6b4fb96d5.jpg",
        caption=f"""╭═★⊷⌯⧼[𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥](https://t.me/source_av)⧽⌯⊶★═╮\n★‹ [𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥𝐀](https://t.me/source_av)\n★‹ [𝐀𝐒𝗞 𝗧𝐎 𝐌𝗘](https://t.me/source_av)\n★‹ [𝙏َِ𝙊َِ𝙈ِ](https://t.me/DEV_TOM)\n★‹ [𝐓𝐎.𝐌𝐄](https://t.me/DEV_TOM)\n╰═★⊷⌯⧼[𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥](https://t.me/source_av)⧽⌯⊶★═╯\n ⍟ Welcome to source Avatar""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙏َِ𝙊َِ𝙈ِ༄►", url=f"https://t.me/DEV_TOM"), 
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥⚡️", url=f"https://t.me/source_av"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/DEVTOM_bot?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



