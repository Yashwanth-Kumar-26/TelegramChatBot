import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import OPENROUTER_API_KEY, USER_SETTINGS, DEFAULT_MODEL

user_conversations = {}  # user_id: list of messages

def get_user_conversation(user_id):
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    return user_conversations[user_id]

def call_openrouter_api(messages, api_key, model):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    if not OPENROUTER_API_KEY:
        await update.message.reply_text("❌ API key not configured in .env")
        return

    model = USER_SETTINGS.get(user_id, {}).get('model', DEFAULT_MODEL)

    conversation = get_user_conversation(user_id)
    conversation.append({"role": "user", "content": user_message})

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

    try:
        ai_response = call_openrouter_api(conversation, OPENROUTER_API_KEY, model)
        conversation.append({"role": "assistant", "content": ai_response})
        keyboard = [
            [InlineKeyboardButton("🔄 Change Model", callback_data="change_model"), InlineKeyboardButton("❓ Help", callback_data="help")]
        ]
        await update.message.reply_text(ai_response, reply_markup=InlineKeyboardMarkup(keyboard))
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")
