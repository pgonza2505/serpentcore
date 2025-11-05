# disnake-bot

A small Discord bot using [disnake] with slash commands, context menus, and a cat fetcher.

## Features
- `/ping` — latency check  
- `/echo` — echo your text  
- `/pfp` — show a user's avatar (supports server avatars & size)  
- `/cat` — random cat from Reddit with a CATAAS fallback  
- `Greet` (user context menu)

## Setup
1. **Python 3.10+**
2. Create a bot in the Developer Portal. Invite it with scopes `bot` and `applications.commands`.
3. Enable intents you actually use.
4. Clone repo & install:
   ```bash
   python -m venv .venv && . .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt