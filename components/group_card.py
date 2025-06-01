import tkinter as tk
from utils.theme_loader import get_group_theme

class GroupCard(tk.Frame):
    def __init__(self, parent, group_name, on_click_callback):
        super().__init__(parent, bd=2, relief="raised")
        theme = get_group_theme(group_name)

        self.configure(bg=theme["color"], padx=10, pady=5)
        self.group_name = group_name
        self.on_click_callback = on_click_callback

        label = tk.Label(self, text=group_name, bg=theme["color"], fg="white", font=("Helvetica", 14, "bold"))
        label.pack(anchor="w")

        motto = tk.Label(self, text=theme["motto"], bg=theme["color"], fg="white", font=("Helvetica", 10, "italic"))
        motto.pack(anchor="w")

        self.bind("<Button-1>", self.on_click)
        label.bind("<Button-1>", self.on_click)
        motto.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        self.on_click_callback(self.group_name)
