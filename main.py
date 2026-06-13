from telegram import Bot
import asyncio
import random

TOKEN = "8706051503:AAH_KAsxWpQ477arAiK_ubBh9gdcxpMcLAM"
CHAT_ID = "7835942427"

messages = [
    "سلام، الان مشغول چه کاری هستی؟ 😊",
    "امروزت چطور گذشت؟",
    "یه اتفاق جالب امروزت رو برام تعریف کن.",
    "حالت الان چطوره؟",
    "امیدوارم روز خوبی داشته باشی 🌷"
]

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=random.choice(messages)
    )

asyncio.run(send_message())
