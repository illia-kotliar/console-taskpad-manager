import json
def load_tasks():
    try:
        with open("saved_tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(transport):
            with open("saved_tasks.json", "w", encoding="utf-8") as file:
                json.dump(transport, file, ensure_ascii=False, indent=4)
