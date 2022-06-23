from NIXA.main import bot
from pyrogram import filters


@bot.on_message(filters.command('ايدي'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ايديك**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**ايدي المجموعة**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ايديك**: `{message.from_user.id}`\n**ايدي المجموعة**: `{message.chat.id}`"
        )
