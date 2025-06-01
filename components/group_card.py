import tkinter as tk
from tkinter import ttk

def create_group_card(parent, group_data, on_click):
    frame = ttk.Frame(parent, padding=10)
    frame.pack(fill='x', pady=5)

    # Use group name and motto
    name = group_data.get("group_name", "Unnamed Group")
    motto = group_data.get("motto", "")

    theme_color = group_data.get("theme_color", "lightgray")  # ✅ Updated key

    label = tk.Label(frame, text=name, font=('Arial', 14, 'bold'), bg=theme_color)
    label.pack(fill='x')

    sublabel = tk.Label(frame, text=motto, font=('Arial', 10), bg=theme_color)
    sublabel.pack(fill='x')

    frame.bind("<Button-1>", lambda e: on_click(group_data))
    label.bind("<Button-1>", lambda e: on_click(group_data))
    sublabel.bind("<Button-1>", lambda e: on_click(group_data))

    return frame
