from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import json

def load_models(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🆓 Free Models", callback_data="free_models"), InlineKeyboardButton("💎 Premium Models", callback_data="premium_models")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings"), InlineKeyboardButton("📖 Help", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)

def model_selection_keyboard(models, model_type):
    keyboard = []
    row = []
    for i, model in enumerate(models):
        row.append(InlineKeyboardButton(f"{model['name']}", callback_data=f"select_model|{model_type}|{model['id']}"))
        if (i + 1) % 2 == 0:  # Every 2 buttons, start new row
            keyboard.append(row)
            row = []
    if row:  # Add remaining buttons
        keyboard.append(row)
    keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

def model_confirm_keyboard(model_id, model_type):
    keyboard = [
        [InlineKeyboardButton("✅ Confirm", callback_data=f"confirm_model|{model_type}|{model_id}")],
        [InlineKeyboardButton("❌ Cancel", callback_data=f"cancel_model|{model_type}")]
    ]
    return InlineKeyboardMarkup(keyboard)

def settings_keyboard():
    keyboard = [
        [InlineKeyboardButton("👁️ Verify API Key", callback_data="verify_api_key")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def help_keyboard():
    keyboard = [
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_keyboard():
    keyboard = [
        [InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(keyboard)
