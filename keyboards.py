from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🛍️ الخدمات", callback_data="services")
        ],
        [
            InlineKeyboardButton("💳 المحفظة", callback_data="wallet"),
            InlineKeyboardButton("📦 طلباتي", callback_data="orders")
        ],
        [
            InlineKeyboardButton("👤 حسابي", callback_data="account"),
            InlineKeyboardButton("🎁 الدعوات", callback_data="referrals")
        ],
        [
            InlineKeyboardButton("💬 الدعم الفني", callback_data="support")
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
