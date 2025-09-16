from telegram import Update
from telegram.ext import ContextTypes
from keyboards import main_menu_keyboard, model_selection_keyboard, model_confirm_keyboard, settings_keyboard, help_keyboard, load_models
from config import USER_SETTINGS, OPENROUTER_API_KEY
from banners import get_banner
import requests

FREE_MODELS = load_models('models_free.json')
PREMIUM_MODELS = load_models('models_premium.json')

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    if data == "free_models":
        text = "🆓 *Free Models*\n\nChoose a model:"
        await query.edit_message_text(text, reply_markup=model_selection_keyboard(FREE_MODELS, "free"), parse_mode='Markdown')
    elif data == "premium_models":
        text = "💎 *Premium Models*\n\nChoose a model:"
        await query.edit_message_text(text, reply_markup=model_selection_keyboard(PREMIUM_MODELS, "premium"), parse_mode='Markdown')
    elif data.startswith("select_model|"):
        parts = data.split("|")
        model_type = parts[1]
        model_id = parts[2]
        models = FREE_MODELS if model_type == "free" else PREMIUM_MODELS
        model = next((m for m in models if m['id'] == model_id), None)
        if model:
            text = f"""
╔══════════════════╗
   🤖 {model['name']}
╚══════════════════╝

{model['description']}

Confirm your selection?
"""
            await query.edit_message_text(text, reply_markup=model_confirm_keyboard(model_id, model_type), parse_mode='Markdown')
    elif data.startswith("confirm_model|"):
        parts = data.split("|")
        model_type = parts[1]
        model_id = parts[2]
        USER_SETTINGS[user_id] = {'model': model_id}
        text = "🚀 All Set! Start Chatting"
        await query.edit_message_text(text, reply_markup=main_menu_keyboard())
    elif data.startswith("cancel_model|"):
        parts = data.split("|")
        model_type = parts[1]
        text = f"❌ Cancelled {model_type} model selection."
        await query.edit_message_text(text, reply_markup=main_menu_keyboard())
    elif data == "settings":
        text = "⚙️ *Settings*\n\nManage your preferences:"
        await query.edit_message_text(text, reply_markup=settings_keyboard(), parse_mode='Markdown')
    elif data == "change_model":
        text = """
╔══════════════════╗
   🤖 Change Model
╚══════════════════╝

Choose a new model:
"""
        await query.edit_message_text(text, reply_markup=main_menu_keyboard(), parse_mode='Markdown')
    elif data == "verify_api_key":
        if OPENROUTER_API_KEY:
            # Test the API key with a simple request
            try:
                url = "https://openrouter.ai/api/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                }
                data_payload = {
                    "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
                    "messages": [{"role": "user", "content": "Hello"}],
                    "max_tokens": 10
                }
                response = requests.post(url, headers=headers, json=data_payload, timeout=10)
                if response.status_code == 200:
                    text = "✅ Working API Key! The instance is ready."
                else:
                    text = f"❌ API Key Error: {response.status_code}"
            except Exception as e:
                text = f"❌ API Test Failed: {str(e)}"
        else:
            text = "❌ No API Key configured in .env"
        await query.edit_message_text(text, reply_markup=settings_keyboard())
    elif data == "help":
        text = """
📖 *Help Menu*

1. Go to Free or Premium Models.
2. Confirm your selection.
3. When you see "All Set 🚀", start chatting!
"""
        await query.edit_message_text(text, reply_markup=help_keyboard(), parse_mode='Markdown')
    elif data == "back_to_main":
        text = get_banner()
        await query.edit_message_text(text, reply_markup=main_menu_keyboard(), parse_mode='Markdown')
