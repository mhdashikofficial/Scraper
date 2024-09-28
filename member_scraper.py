from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

async def scrape_members(client, group_name):
    dialogs = await client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer=InputPeerEmpty(), limit=200))
    for dialog in dialogs.chats:
        if dialog.title == group_name:
            participants = await client.get_participants(dialog, aggressive=True)
            members = [{'id': p.id, 'name': p.first_name} for p in participants]
            # Save members to file or return them as a list
            with open(f"{group_name}_members.txt", 'w') as f:
                for member in members:
                    f.write(f"{member['id']},{member['name']}\n")
            return members
