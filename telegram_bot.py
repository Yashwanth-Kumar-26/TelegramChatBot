#!/usr/bin/env python3
"""
Telegram AI Assistant Starter Bot
OpenRouter Integration with InlineKeyboard menus
"""

import logging
import os
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from handlers.start import start_handler
from handlers.callbacks import callback_handler
from handlers.chat import chat_handler

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def message_handler(update, context):
    await chat_handler(update, context)

def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set in environment variables.")
        return

    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start_handler))

    # Callback handler for inline keyboards
    application.add_handler(CallbackQueryHandler(callback_handler))

    # Message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    application.run_polling()

if __name__ == '__main__':
    main()
