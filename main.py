import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import google.generativeai as genai

BOT_TOKEN = os.environ["BOT_TOKEN"]
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
user_text = update.message.text

```
prompt = f"""
تو یک دوست صمیمی فارسی‌زبان هستی.
طبیعی، دوستانه و کوتاه جواب بده.
اسم کاربر را نمی‌دانی.
متن کاربر:
{user_text}
"""

try:
    response = model.generate_content(prompt)
    await update.message.reply_text(response.text)
except Exception:
    await update.message.reply_text("الان نمی‌تونم جواب بدم، بعداً دوباره امتحان کن.")
```

def main():
app = Application.builder().token(BOT_TOKEN).build()

```
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("Bot Started...")
app.run_polling()
```

if **name** == "**main**":
main()
