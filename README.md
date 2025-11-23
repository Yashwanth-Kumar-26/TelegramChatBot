# 🤖 TeleChatbot - Open-Source AI Assistant

An advanced Telegram bot powered by OpenRouter, featuring multiple AI models, interactive menus, and a sleek user interface.

## ✨ Features

### 🚀 Core Functionality
- **Multi-Model Support**: Choose from 8+ Free and 5+ Premium AI models
- **OpenRouter Integration**: Seamless API integration with real-time responses
- **Conversation History**: Maintains chat context for natural conversations
- **Inline Menus**: Fully keyboard-driven navigation (no commands needed)

### 🎨 User Experience
- **Random Banners**: 13 different ASCII art welcome screens
- **Emoji-Rich Interface**: Cool emojis throughout the bot
- **Side-by-Side Layouts**: Modern button arrangements
- **Interactive Responses**: Change model and help buttons after each AI reply

### ⚙️ Management
- **Global API Key**: Single OpenRouter key for all users
- **Per-User Model Selection**: Each user can choose their preferred model
- **API Verification**: Test your API key directly in the bot
- **Settings Menu**: Easy configuration options

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- OpenRouter API Key (from [OpenRouter](https://openrouter.ai))

### Setup Steps

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone https://github.com/Yashwanth-Kumar-26/TelegramChatBot.git
   cd TelegramChatBot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Rename `env.example` to `.env` and update the values:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. **Run the Bot**
   ```bash
   python telegram_bot.py
   ```

## 📖 Usage

### Getting Started
1. Start a chat with your bot on Telegram
2. Use `/start` or send any message to begin
3. You'll see a random welcome banner with menu options

### Navigation
- **🆓 Free Models**: Access free AI models (no API costs)
- **💎 Premium Models**: Access paid models (requires API credits)
- **⚙️ Settings**: Verify API key and manage preferences
- **📖 Help**: View usage instructions

### Model Selection
1. Choose Free or Premium models
2. Browse available models (displayed 2 per row)
3. Tap a model to see details and confirm
4. Once confirmed, start chatting!

### Chatting
- Send any message to chat with the selected AI
- Each response includes "🔄 Change Model" and "❓ Help" buttons
- Conversation history is maintained automatically

## 🏗️ Project Structure

```
TeleChatbot/
├── telegram_bot.py          # Main bot application
├── config.py               # Configuration and constants
├── banners.py              # Random welcome banners
├── keyboards.py            # Inline keyboard definitions
├── models_free.json        # Free AI models configuration
├── models_premium.json     # Premium AI models configuration
├── handlers/
│   ├── start.py           # Start command handler
│   ├── callbacks.py       # Inline button callbacks
│   ├── chat.py            # Chat message handling
│   └── key_input.py       # API key input (legacy)
├── .env.example            # Environment variables template
└── README.md              # This file
```

## ⚙️ Configuration

### Environment Variables (.env)
```env
BOT_TOKEN="@your_telegram_bot_token"
OPENROUTER_API_KEY="@your_api_key"
```

### Model Configuration
Models are defined in JSON files:
- `models_free.json`: Free models with no API costs
- `models_premium.json`: Premium models requiring credits

Each model entry:
```json
{
  "id": "model-identifier",
  "name": "🧠 Display Name",
  "description": "Description with emojis ✨"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding New Models
1. Find the model ID on [OpenRouter](https://openrouter.ai/models)
2. Add to appropriate JSON file (free or premium)
3. Include cool emojis in name and description
4. Test the integration

### Adding Banners
1. Create ASCII art in `banners.py`
2. Add to the `banners` list
3. Ensure Markdown compatibility

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [OpenRouter](https://openrouter.ai) for the AI API
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library
- All the amazing open-source AI models available

## 🆘 Troubleshooting

### Bot doesn't respond
- Check if BOT_TOKEN is correct
- Ensure the bot is running (`python telegram_bot.py`)
- Verify internet connection

### API errors
- Confirm OPENROUTER_API_KEY is valid
- Check API credits/billing on OpenRouter
- Use "Verify API Key" in bot settings

### Model not working
- Ensure the model ID is correct in JSON files
- Check if the model is available on OpenRouter
- Try selecting a different model

## 📞 Support

For issues or questions:
1. Check this README
2. Review the code comments
3. Open an issue on GitHub
4. Join our community discussions

---

# **Made with ❤️ for the open-source AI community**
# **Developed with  by Siddu ❤️(Team Chanakya Circle)**
