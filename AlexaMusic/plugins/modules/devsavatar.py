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

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين افاتار","المطورين","مطورين"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/aa84897eb42d6b4fb96d5.jpg",
        caption=f"""**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين افاتار ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙏َِ𝙊َِ𝙈ِ⌯‹♱༄►", url=f"https://t.me/DEV_TOM"), 
                 ],[
                    InlineKeyboardButton(
                        "ρ᥆kᥱꪔ᥆ꪀ", url=f"https://t.me/devpokemon"),
                    InlineKeyboardButton(
                        "𝐊𝐈𝐍𝐆", url=f"https://t.me/TR_E2S_ON_MY_MOoN"),
                ],[
                    InlineKeyboardButton(
                        "𝐶𝑅𝐼𝑆𝑇𝐼𝑁", url=f"https://t.me/dr_criss"),
                    InlineKeyboardButton(
                        "ꪔᥲ️ꪀ᥆᥆", url=f"https://t.me/C1_I_I"),
                ],[
                
                    InlineKeyboardButton(
                        "★𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥⚡", url=f"https://t.me/source_av"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["توم انجم","احمد","توم","مبرمج","TOM","tom"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("DEV_TOM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين انجم","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
