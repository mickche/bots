
import json


def save_data(user_id, new_data):
    with open('data.json', 'r', encoding="utf-8") as f:
        data = json.load(f)

    if str(user_id) not in data:
        data[str(user_id)] = []

    data[str(user_id)].append(new_data)

    with open('data.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_data(user_id):
    with open('data.json', 'r', encoding="utf-8") as f:
        data = json.load(f)

    return data.get(str(user_id))
