import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8506879373:AAGqdWa3RNJUbatMJeEZy53hKtOdpLCz5C0")

# START MENU
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Create Deal", "Help"],
        ["Dispute"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    text = """
💫 Welcome to Pagal Escrow Bot 💫

Safe & Secure Telegram Escrow Service

Commands:
/deal - Create new deal
/release - Release funds
/dispute - Open dispute
/help - Help menu
"""

    await update.message.reply_text(text, reply_markup=reply_markup)


# CREATE DEAL
async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Send deal details in format:\n\nBuyer @username\nSeller @username\nAmount\nDescription"
    )


# RELEASE FUNDS
async def release(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Funds released to seller."
    )


# DISPUTE
async def dispute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ Dispute opened.\nAdmin will join within 24 hours."
    )


# HELP
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Help Menu

/deal - Create escrow deal
/release - Release funds
/dispute - Open dispute
"""
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("deal", deal))
    app.add_handler(CommandHandler("release", release))
    app.add_handler(CommandHandler("dispute", dispute))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
