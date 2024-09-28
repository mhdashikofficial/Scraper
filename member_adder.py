from telethon.tl.functions.channels import InviteToChannel

async def add_members(client, group_name, member_list_file):
    with open(member_list_file, 'r') as f:
        members = [line.strip().split(',') for line in f.readlines()]

    dialogs = await client.get_dialogs()
    target_group = None
    for dialog in dialogs:
        if dialog.title == group_name:
            target_group = dialog
            break

    if target_group:
        for member_id, name in members:
            try:
                await client(InviteToChannel(target_group, [int(member_id)]))
                print(f"Added {name} to {group_name}")
                time.sleep(2)  # Avoid getting blocked
            except Exception as e:
                print(f"Error adding {name}: {str(e)}")
    else:
        print(f"Group {group_name} not found")
