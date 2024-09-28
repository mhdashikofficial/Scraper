from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH

async def authenticate(phone, api_id, api_hash, session_str=None):
    client = TelegramClient(StringSession(session_str), api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input('Enter the code: ')
        await client.sign_in(phone, code)
    return client

async def add_new_account(api_id, api_hash, phone):
    """Handles a new session for a new account."""
    client = await authenticate(phone, api_id, api_hash)
    session = StringSession.save(client.session)
    return session
