import os
import logging
import logging.config 

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING) 

from .commands import start
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
OWNER_ID = os.environ.get("OWNER_ID") 

@Client.on_callback_query(Filters.regex('^help$'))
async def help_cb(c, m): 
  await m.answer() 
  
  # help text 
  help_text = """**💥 Hey You Need Help ?**

**1. Send Me The Telegram File Or Video Which You Wanted To Convert.

2. Send Me The Thumbnail [ Photo ]. [ Optional ]

3. Reply To Video /CTF For Converting Into File.

4. Reply To File /CTV For Converting Into Video.**

**🔍 Support Channel :** [MS Bot Updates](https://telegram.dog/MSBOTCREATERS)

"""
  
  # creating buttons 
  buttons = [ [ InlineKeyboardButton('🏠 Home', callback_data='home'), InlineKeyboardButton('⁉️ About', callback_data='about') ], [ InlineKeyboardButton('💠 Close', callback_data='close') ] ] 
  
  # editing as help message 
  await m.message.edit( text=help_text, 
                       reply_markup=InlineKeyboardMarkup(buttons) ) 
  
  @Client.on_callback_query(Filters.regex('^close$'))
  async def close_cb(c, m): 
    await m.message.delete() 
    await m.message.reply_to_message.delete()
 
  @Client.on_callback_query(Filters.regex('^about$'))
  async def about_cb(c, m):
    await m.answer()
    

    # about text
    about_text = """

**📝 Language : Python 3**

**🧰 Framework : Pyrogram**

**👨🏻‍💻 Developer :** [Shadab](https://t.me/Shadab_Alam)

**🔍 Channel :** [MS BOT UPDATES](https://t.me/MSBOTCREATERS)

"""
    
    # creating buttons
    buttons = [

        [

            InlineKeyboardButton('🏠 Home', callback_data='home'),

            InlineKeyboardButton('👨🏻‍💻 Help', callback_data='help')

        ],

        [

            InlineKeyboardButton('💠 Close', callback_data='close')

        ]

    ]

    # editing message
   await m.message.edit(
                    text=about_text,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    disable_web_page_preview=True
    )

@Client.on_callback_query(Filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)
