from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

✦ ɪ ᴀᴍ ๛sᴛʀᴀɴɢᴇʀ༗

✦ sᴛʀᴀɴɢᴇʀ ᴘᴀᴘᴀ ʜ ʙʜᴀɪ ᴛᴜᴍ sᴀʙᴋᴇ .

✦ ʜᴇʏ ɪ ᴀᴍ ᴀʟᴇxᴀ  ᴍᴀᴅᴇ ʙʏ → sᴛʀᴀɴɢᴇʀ ᴏᴘ✨.
**"""




@app.on_message(filters.command("Owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/strangers_bots"),
          InlineKeyboardButton("ᴅᴍ ᴏғ sᴛʀᴀɴɢᴇʀ ᴘᴀᴘᴀ ", url="https://t.me/NoMoreTyMWaStE"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c37df67b6ea049c97c2bd.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
