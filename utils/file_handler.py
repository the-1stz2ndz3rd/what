import json
import os

def read_json(filepath):
    """Reads and returns JSON data from a file."""
    if not os.path.exists(filepath):
        # Return a default empty structure based on file type
        if filepath.endswith("users.json"):
            return []
        else:
            return {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"[ERROR] Failed to decode JSON in {filepath}. Returning empty.")
        return [] if filepath.endswith("users.json") else {}

def write_json(filepath, data):
    """Writes JSON data to a file."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[ERROR] Failed to write to {filepath}: {e}")
