import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "╔══════════════════════╗\n"
        "     ✦ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗕𝗢𝗧 ✦\n"
        "╚══════════════════════╝\n\n"
        "أهلاً بيك 👑\n"
        "البوت شغال بنجاح 🚀"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN غير موجود")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 BOT IS RUNNING")
    app.run_polling()


if __name__ == "__main__":
    main()
