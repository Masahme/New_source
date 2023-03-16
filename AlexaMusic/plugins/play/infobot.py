import os
from strings.filters import command
from pyrogram import filters
from pyrogram.types import Message
from YukkiMusic import app
from YukkiMusic.core.vampirs import vampir


async def get_user_info(user, already=False):
    if not already:
        user = await app.get_users(user)
    if not user.first_name:
        return ["حساب محذوف", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("👮🏼‍♂️ رابط المستخدم️")
    dc_id = user.dc_id
    photo_id = user.photo.big_file_id if user.photo else None
    vambir = {
        "الايدي🆔": user_id,
        "المستوي📟": dc_id,
        "الاسم🙋🏼‍♂️": first_name,
        "اليوزر📧": [("@" + username) if username else "لايوجد يوزر"],
        "الرابط➿️": [mention],
    }
    caption = vampir("◍ معلومات الحساب √", vambir)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam    
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[رابط المجموعه🌐](t.me/{username})" if username else "لايوجد رابط"
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    vambir = {
        "ايدي الجروب🆔": chat_id,
        "المستوي🗃": dc_id,
        "نوع المجموعه🗽": type_,
        "الاسم🌐": [title],
        "اليوزر📧": [("@" + username) if username else "لايوجد يوزر"],
        "الرابط➿": [link],
        "عدد الاعضاء📟": members,
        "الاحتيال☣️": is_scam,
        "حالة التقييد⚠️": is_restricted,        
        "البايو🎊": description,
    }
    caption = vampir("◍ معلومات المجموعة √", vambir)
    return [caption, photo_id]


@app.on_message(command("ايدي") & filters.private & ~filters.edited)
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("◍ جاري جلب الايدي.... √")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await app.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)


@app.on_message(command("معلومات") & filters.private & ~filters.edited)
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "استخدم:معلومات+ [USERNAME|ID]"
            )

        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]

        m = await message.reply_text("◍ جاري جلب المعلومات... √")

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await app.download_media(photo_id)
        await message.reply_photo(photo, caption=info_caption, quote=False)

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)
