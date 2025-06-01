import json
import os

GROUPS_FILE = os.path.join("data", "groups.json")

def get_theme_for_group(group_name):
    try:
        with open(GROUPS_FILE, "r") as f:
            groups = json.load(f)
        group_info = groups.get(group_name, {})
        return group_info.get("theme_color", "lightgray")  # ✅ Updated key
    except Exception as e:
        print(f"Error loading theme for group {group_name}: {e}")
        return "lightgray"

def apply_theme(widget, color_name):
    try:
        widget.configure(bg=color_name)
        for child in widget.winfo_children():
            try:
                child.configure(bg=color_name)
            except:
                pass
    except:
        pass
