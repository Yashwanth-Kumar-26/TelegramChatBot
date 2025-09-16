from telegram import Update
from telegram.ext import ContextTypes
from config import USER_KEYS
from keyboards import settings_keyboard

async def key_input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if context.user_data.get('awaiting_key'):
        key = update.message.text.strip()
        if key.startswith('sk-') and len(key) > 10:
            USER_KEYS[user_id] = key
            await update.message.reply_text("✅ API Key set successfully!", reply_markup=settings_keyboard())
        else:
            await update.message.reply_text("❌ Invalid API key format. Please send a valid OpenRouter key starting with 'sk-'.", reply_markup=settings_keyboard())
        context.user_data['awaiting_key'] = False
    else:
        # If not awaiting key, perhaps pass to chat handler
        pass
