import json
from tkinter import Widget

def get_group_theme(group_name):
    try:
        with open("data/groups.json", "r") as f:
            groups = json.load(f)
        group_data = groups.get(group_name)
        if group_data:
            return {
                "color": group_data.get("theme_color", "#cccccc"),
                "motto": group_data.get("motto", ""),
            }
    except FileNotFoundError:
        pass
    return {"color": "#cccccc", "motto": ""}

def apply_theme(widget: Widget, group_name: str):
    theme = get_group_theme(group_name)
    widget.configure(bg=theme["color"])
