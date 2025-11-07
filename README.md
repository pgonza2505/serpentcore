# disnake-bot

A small Discord bot using [disnake] with slash commands, context menus, and a handful of fun, utility, and moderation-style tools.

## Features
### 🎮 Core Commands
`/ping` — check bot latency

`/echo` — echo back your message

`/pfp` — show a user's profile picture (supports server avatars & custom sizes)

`Greet` (user context menu) — greet any user directly from the context menu

### 🐾 Fun & Entertainment
`/cat` — random cat image from Reddit with CATAAS fallback

`/dog` — random dog image from Random.Dog

`/meme` — fetch a meme from subreddits like r/memes, r/dankmemes, or r/wholesomememes

`/quote` — get an inspirational, humorous, or famous quote

`/eightball` — ask the magic 8-ball a question (rare chance of a rude response)

`/roll` — roll customizable dice (e.g. 3d6 + 2)

### 🧰 Utility & Quality-of-Life
`/userinfo` — view information about a user (roles, join date, account age)

`/serverinfo` — view server statistics and creation info

`/remindme` — set a reminder with custom delay and optional DM delivery

`/poll` — create a quick reaction-based poll with up to 5 options

`/stats` — check bot stats, uptime, and latency

`/define` — look up English word definitions

## Setup
1. **Python 3.10+**
2. Create a bot in the Developer Portal. Invite it with scopes bot and applications.commands.
3. Enable only the intents you actually need.
4. Clone the repo & install dependencies:
```bash
python -m venv .venv && . .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
5. Create a .env file (based on .env.example) and add your bot token.

## Run
```bash
python bot.py
```

## Developer Tips
- Add `guild_ids=[YOUR_GUILD_ID]` in slash command decorators for instant sync while testing.
- Remove it for global availability once stable (global sync may take up to an hour).
- Use `Ctrl+R` in Discord to hard-reload if commands don’t appear after syncing.
