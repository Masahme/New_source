import asyncio
import pyrogram
import random
from datetime import datetime
import pytz
from AlexaMusic import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)








def cairo_time():
    return datetime.now(pytz.timezone('Africa/Cairo'))

welcome_enabled = True

@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    """Send a welcome message to new members."""
    if not welcome_enabled:
        return

    if chat_member_updated.new_chat_member:
        user = chat_member_updated.new_chat_member.user
        message = (
            f" •نورت الجروب يا {user.first_name}!\n"
            f"\n"
            f"•من فضلك التزم بالقوانين الجروب\n"
            f"\n"
            f"•يوزرك  >> @{user.username}\n"
            f"\n"
            f"•الايدي بتاعك  >> {user.id}\n"
            f"\n"
            f"•تاريخ انضمامك  >> {cairo_time().strftime('%Y-%m-%d')}\n"
            f"\n"
            f"•وقت انضمامك  >> {cairo_time().strftime('%H:%M:%S')}"
        )

        inline_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(user.first_name, url=f"https://t.me/{user.username}")
                ],
                [
                     InlineKeyboardButton(text="𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗩𝗔𝗧𝗔𝗥", url=f"https://t.me/source_av")
                ]         
            ]
        )

        await client.send_photo(
            chat_id=chat_member_updated.chat.id,
            photo="https://telegra.ph/file/aa84897eb42d6b4fb96d5.jpg",
            caption=message,
            reply_markup=inline_keyboard
        )


@app.on_message(filters.group & SUDOERS)
async def toggle_welcome(client, message):
    global welcome_enabled
    
    if message.text == "تفعيل الترحيب":
        welcome_enabled = True
        await message.reply("تم تفعيل الترحيب بنجاح!")
    elif message.text == "إيقاف الترحيب":
        welcome_enabled = False
        await message.reply("تم إيقاف الترحيب بنجاح!")



