# Telegram Scraping and Bulk Messaging Bot

## Overview

This bot supports:
- Member scraping from Telegram groups
- Bulk messaging with support for filtering (active/premium users)
- Adding scraped members to other groups
- Multi-account session management

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mhdashikofficial/Scraper.git
Install dependencies:
bash
Copy code


pip install -r requirements.txt
Configure your config.py file with your API ID, API Hash, and Bot Token.

Run the bot:

bash
Copy code
python bot.py
Usage
Use the /start command to begin the authentication process.
Once authenticated, you can choose to:
Scrape members from a group
Send bulk messages to members
Add members to another group
Passkey
The default passkey is vip666. Modify this in bot.py for security.

yaml
Copy code

---










