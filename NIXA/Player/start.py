import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from NIXA.filters import command
from NIXA.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from NIXA.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**هلا حبيب 
يمكنك تشغيل الاغاني بإستخدامي في المكالمات الصوتية
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضفني الى مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📜|الاوامر", url=f"https://telegra.ph/%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B3%D9%88%D8%B1%D8%B3-%D8%AA%D9%8A%D8%A8%D8%AB%D9%88%D9%86-06-23"
                    ),
                    InlineKeyboardButton(
                        "", url="https://t.me/Simple_Mundaa"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " 🌐|السورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        " ❓|كروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["السورس", "سورس"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2f6762e96eab0a1ef3644.jpg",
        caption=f"""اهلا بك في سورس تيبثون افضل السورسات على الاطلاق التنصيبات مجانيه انضم للقناة لكي تنصب بوتك الخاص ام اكتب المبرمج لتنصيب مدفوع.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🖥️|قناة السورس", url=f"https://t.me/Tepthon")
                ]
            ]
        ),
    )


@Client.on_message(command(["المبرمج", "مبرمج"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc2d9bcb1ff3adcb3313.jpg",
        caption=f"""اهلا بك يمكنك التواصل مع محمد تيبثون الان""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐷𝐸𝑉 𝑀𝑂𝐻𝐴𝑀𝑀𝐴𝐷 𝅘𝅥𝅯", url=f"https://t.me/P17_12")
                ]
            ]
        ),
    )
