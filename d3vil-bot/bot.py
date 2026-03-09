from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8606167168:AAGiUyxVwHjMkOqgZHOY61XBN8phc_4l_Mg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
💫 Welcome to D3VIL Escrows 💫
Your Trustworthy Telegram Escrow Service

Welcome to @d3vil_escrowbot. This bot provides a reliable escrow service for your transactions on Telegram.

Avoid scams, your funds are safeguarded throughout your deals. If you run into any issues, simply type /dispute and an arbitrator will join the group chat within 24 hours.

🎟 ESCROW FEE:
1.0% for P2P and 1.0% for OTC Flat

🌐 UPDATES & VOUCHES:
@thed3vilnetwork

💬 Proceed with /escrow (to start with a new escrow)

⚠️ IMPORTANT:
Make sure coin is same of Buyer and Seller else you may lose your coin.

💡 Type /menu to summon a menu with all bots features
""")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
