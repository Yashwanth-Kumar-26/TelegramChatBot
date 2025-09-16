from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_menu_keyboard
from banners import get_banner

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = get_banner()
    await update.message.reply_text(welcome_text, reply_markup=main_menu_keyboard())
