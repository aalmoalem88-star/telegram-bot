from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import init_db, add_user
from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
    )

    text = (
        "╔══════════════════════════╗\n"
        "      ✦ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗕𝗢𝗧 ✦\n"
        "╚══════════════════════════╝\n\n"
        f"أهلاً بيك {user.first_name} 👑\n\n"
        "💎 أهلاً بيك في متجرنا\n"
        "⚡ خدمات سريعة ومنظمة\n"
        "🔐 حسابك محفوظ بأمان\n\n"
        "اختار من القائمة 👇"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    messages = {
        "services": "🛍️ الخدمات\n\nقسم الخدمات هيكون جاهز قريبًا.",
        "wallet": "💳 المحفظة\n\n💰 رصيدك الحالي: 0.00$",
        "orders": "📦 طلباتي\n\nمفيش طلبات حتى الآن.",
        "account": "👤 حسابك\n\nحسابك اتسجل بنجاح.",
        "referrals": "🎁 الدعوات\n\nنظام الإحالة هيتم إضافته قريبًا.",
        "support": "💬 الدعم الفني\n\nالدعم الفني هيتم تفعيله قريبًا.",
    }

    message = messages.get(
        query.data,
        "اختيار غير معروف."
    )

    await query.message.edit_text(
        message,
        reply_markup=main_menu()
    )


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("🚀 TELEGRAM BOT IS RUNNING")

    app.run_polling()


if __name__ == "__main__":
    main() 
