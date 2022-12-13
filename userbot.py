from asyncio import sleep
from pyrogram import Client, filters

app = Client("farxann711")
spam_text = 'sen qehbesen'

@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    cmd = message.text.split()
    await message.reply_text(spam_text)

app.run()
