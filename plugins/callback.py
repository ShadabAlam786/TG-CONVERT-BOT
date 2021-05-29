import os
import logging
import logging.config 

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING) 

from .commands import start, BATCH
from pyrogram import Client, filters
from pyrogram.types import 
InlineKeyboardButton, InlineKeyboardMarkup
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
OWNER_ID = os.environ.get("OWNER_ID") 

@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m): 
  await m.answer() 
  
  # help text 
  help_text = """**You need Help?? 🧐
  **★ Just send me the files i will store file and give you share able link**You can use me in channel too 😉**★ Make me admin in your channel with edit permission. Thats enough now continue uploading files in channel i will edit all posts and add share able link url buttons""" 
  
  # creating buttons 
  buttons = [ [ InlineKeyboardButton('Home 🏕', callback_data='home'), InlineKeyboardButton('About 📕', callback_data='about') ], [ InlineKeyboardButton('Close 🔐', callback_data='close') ] ] 
  
  # editing as help message 
  await m.message.edit( text=help_text, 
                       reply_markup=InlineKeyboardMarkup(buttons) ) 
  
  @Client.on_callback_query(filters.regex('^close$'))async def close_cb(c, m): await m.message.delete() await m.message.reply_to_message.delete()
