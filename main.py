from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters,
)
import os

TOKEN = os.environ["8706051503:AAH_KAsxWpQ477arAiK_ubBh9gdcxpMcLAM"]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        f"پیامت رو گرفتم 😊\n\nتو گفتی:\n{user_text}"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

print("Bot is running...")
app.run_polling()
