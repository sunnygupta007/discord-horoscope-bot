# Discord Bot - Taino

A Discord bot that provides daily, weekly, and monthly horoscopes, career insights, money forecasts, health predictions, and inspirational quotes.

## Features

- **Daily Horoscope** - Get your daily horoscope for any zodiac sign
- **Weekly Horoscope** - Get your weekly horoscope forecast
- **Monthly Horoscope** - Get your monthly horoscope predictions
- **Career Insights** - Get career-related predictions
- **Money Forecast** - Get weekly money and finance predictions
- **Health Predictions** - Get daily health and wellness insights
- **Inspirational Quotes** - Get random inspirational quotes
- **Interactive Commands** - Various fun commands like roll dice, greetings, and more

## Prerequisites

- Python 3.8 or higher
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications)

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd Discord-Bot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Setup

1. Create a Discord application and bot at the [Discord Developer Portal](https://discord.com/developers/applications)
2. Get your bot token from the "Bot" section
3. Create a `.env` file in the project root (use `.env.example` as a template):
```bash
cp .env.example .env
```

4. Edit the `.env` file and add your Discord bot token:
```
DISCORD_TOKEN=your_actual_discord_bot_token_here
```

5. Invite your bot to your server using the OAuth2 URL generator in the Discord Developer Portal with the following permissions:
- Read Messages/View Channels
- Send Messages
- Read Message History

## Usage

Run the bot:
```bash
python main.py
```

## Available Commands

### Main Commands
- `$daily <zodiac_sign>` - Get daily horoscope (e.g., `$daily aries`)
- `$weekly <zodiac_sign>` - Get weekly horoscope
- `$monthly <zodiac_sign>` - Get monthly horoscope
- `$career <zodiac_sign>` - Get career insights
- `$money <zodiac_sign>` - Get money forecast
- `$health <zodiac_sign>` - Get health predictions
- `$inspire` - Get a random inspirational quote

### Other Commands
- `$hello` - Greet the bot
- `$hey` - Say hey to the bot
- `$ping` - Get the list of all available commands
- `$thanks` - Thank the bot
- `$how are you` - Ask how the bot is doing
- `$bye` - Say goodbye
- `$sorry` - Apologize to the bot
- `$no` - Say no to the bot
- `$roll dice` - Roll a dice (1-12)

### Zodiac Signs
The bot supports all 12 zodiac signs (case-insensitive):
- aries, taurus, gemini, cancer, leo, virgo
- libra, scorpio, sagittarius, capricorn, aquarius, pisces

## Project Structure

```
Discord-Bot/
├── main.py           # Main bot logic and command handlers
├── responses.py      # Helper functions for bot responses
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Dependencies

- `discord.py` - Discord API wrapper
- `requests` - HTTP library for web scraping
- `beautifulsoup4` - HTML parsing for horoscope data
- `python-dotenv` - Environment variable management

## Troubleshooting

- If the bot doesn't respond, ensure the bot has the necessary permissions in your server
- Make sure your Discord token is correct in the `.env` file
- Check that you've enabled Message Content Intent in the Discord Developer Portal for your bot

## Security Notes

- Never commit your `.env` file to version control
- Never share your Discord bot token publicly
- The `.gitignore` file is configured to prevent committing sensitive files
