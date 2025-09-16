import random

# ──────────────── ALL BANNERS ──────────────── #

banner1 = """
╔══════════════════╗
   🤖 Welcome to Your Bot
╚══════════════════╝

✨ Open-source AI Assistant
Choose an option below:
"""

banner2 = """
╭──────────────────────────╮
   🚀 Welcome to AI Assistant
╰──────────────────────────╯

✨ Open-source, powered by OpenRouter
Pick an option to get started:
"""

banner3 = """
[🤖 AI Assistant Starter Bot]

✨ Build. Chat. Explore.
Your journey starts here ⬇️
"""

banner4 = """
╔════════════════════════╗
║  🤖 AI Assistant Ready! ║
╚════════════════════════╝

✨ Open-source Telegram Bot
Select an option below 👇
"""

banner5 = """
✦━━━━━━━━━━━━━━━━━━━━✦
   🤖 AI Assistant Online
✦━━━━━━━━━━━━━━━━━━━━✦

✨ Explore Free & Premium Models
"""

banner6 = """
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    🤖 Welcome, Explorer!
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈

✨ Open-source AI Assistant
"""

banner7 = """
╔═══ ⚡ AI ASSISTANT ⚡ ═══╗
║  🤖 Powered by OpenRouter ║
╚═══════════════════════════╝

✨ Your open-source AI companion
"""

banner8 = """
▌│█║▌║▌║ 🤖 AI BOT ║▌║▌║█│▌

✨ Hack the chat. Explore the models.
"""

banner9 = """
█████████████████████
█ 🤖 AI Assistant Bot █
█████████████████████

✨ Open-source intelligence, for all.
"""

banner10 = """
◇───────────────◇
   🤖 AI Assistant
◇───────────────◇

✨ Free & Premium Models await!
"""

banner11 = """
>>> 🚀 AI Assistant Online <<<

✨ Choose your path below
"""

banner12 = """
╭──────────────╮
   🤖 AI Assistant
╰──────────────╯

✨ Open-source starter kit
"""

banner13 = """
♛━━━━━━━━━━━━━━♛
   🤖 Master’s AI Bot
♛━━━━━━━━━━━━━━♛

✨ Built with love, open-source forever
"""

# ──────────────── RANDOMIZER ──────────────── #

banners = [
    banner1, banner2, banner3, banner4, banner5,
    banner6, banner7, banner8, banner9, banner10,
    banner11, banner12, banner13
]

def get_banner():
    """Return a random banner each time."""
    return random.choice(banners)
