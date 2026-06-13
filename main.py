from telegram import Bot
import asyncio
import random
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

messages = [
    "سلام 😊 حالت چطوره؟",
    "امروز چه خبر بوده؟",
    "الان داری چیکار می‌کنی؟",
    "یه لیوان آب خوردی؟ 😄",
    "امیدوارم روز خوبی داشته باشی 🌷",
    "یه اتفاق جالب امروزت رو تعریف کن.",
]

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=random.choice(messages)
    )

asyncio.run(send_message())
