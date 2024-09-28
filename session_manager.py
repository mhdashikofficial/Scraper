from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH
import json

def save_session(session_str, account_name):
    with open(f"{account_name}_session.txt", 'w') as f:
        f.write(session_str)

def load_session(account_name):
    with open(f"{account_name}_session.txt", 'r') as f:
        return f.read()

def list_accounts():
    """Lists all saved accounts (sessions)."""
    accounts = []
    for file in os.listdir():
        if file.endswith("_session.txt"):
            accounts.append(file.replace("_session.txt", ""))
    return accounts
