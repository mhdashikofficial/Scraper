from telethon.errors import FloodWaitError
import time

async def send_bulk_message(client, group_name, message, filter_type=None):
    """Sends bulk messages to all or filtered users."""
    with open(f"{group_name}_members.txt", 'r') as f:
        members = [line.strip().split(',') for line in f.readlines()]

    if filter_type == 'active':
        members = await filter_active_users(client, members)
    elif filter_type == 'premium':
        members = await filter_premium_users(members)

    for member_id, name in members:
        try:
            await client.send_message(int(member_id), message)
            time.sleep(2)  # Sleep to avoid Telegram rate limits
        except FloodWaitError as e:
            print(f"Rate limited. Waiting {e.seconds} seconds.")
            time.sleep(e.seconds)

async def filter_active_users(client, members):
    """Filters members based on recent activity (e.g., last 5 days)."""
    active_members = []
    for member_id, name in members:
        user = await client.get_entity(int(member_id))
        if hasattr(user.status, 'was_online'):
            last_seen = user.status.was_online
            if last_seen and (datetime.now() - last_seen).days <= 5:
                active_members.append((member_id, name))
    return active_members

async def filter_premium_users(members):
    """Filters members who have Telegram Premium."""
    return [member for member in members if member.premium]
