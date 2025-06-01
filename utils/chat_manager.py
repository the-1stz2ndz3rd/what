from utils.file_handler import read_json, write_json
from datetime import datetime

GROUP_CHAT_FILE = "data/group_chats.json"
PRIVATE_CHAT_FILE = "data/private_chats.json"

def add_group_message(group_name, sender, message):
    data = read_json(GROUP_CHAT_FILE)
    if group_name not in data:
        data[group_name] = []
    data[group_name].append({
        "sender": sender,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    write_json(GROUP_CHAT_FILE, data)

def get_group_messages(group_name, limit=50):
    data = read_json(GROUP_CHAT_FILE)
    return data.get(group_name, [])[-limit:]

def add_private_message(user1, user2, sender, message):
    key = "_".join(sorted([user1, user2]))
    data = read_json(PRIVATE_CHAT_FILE)
    if key not in data:
        data[key] = []
    data[key].append({
        "sender": sender,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    write_json(PRIVATE_CHAT_FILE, data)

def get_private_messages(user1, user2, limit=50):
    key = "_".join(sorted([user1, user2]))
    data = read_json(PRIVATE_CHAT_FILE)
    return data.get(key, [])[-limit:]
