import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/1b819cfbcb2a2d3c738f6.jpg",
    "https://telegra.ph/file/3021c823c7f006658682f.jpg",
    "https://telegra.ph/file/05561f0fbf323e057ab87.jpg",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/b3de9e03e5c8737ca897f.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ**\n\n"
                f"**📌 ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                f"**🍂 ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n"
                f"**🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ:** @{message.chat.username}\n"
                f"**🛰 ᴄʜᴀᴛ ʟɪɴᴋ:** [ᴄʟɪᴄᴋ]({link})\n"
                f"**📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs:** {count}\n"
                f"**🤔 ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"**✫** <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐈ᴅ :** {chat_id}\n\n**𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ :** {remove_by}\n\n**𝐁ᴏᴛ : @{app.username}**"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
