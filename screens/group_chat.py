import tkinter as tk
from tkinter import messagebox
from components.chat_bubble import ChatBubble
from utils.chat_manager import load_group_messages, save_group_message
from utils.theme_loader import get_theme_for_group

class GroupChatScreen(tk.Frame):
    def __init__(self, parent, controller, group_name, current_user):
        super().__init__(parent)
        self.controller = controller
        self.group_name = group_name
        self.current_user = current_user

        # Apply theme color from group
        theme = get_theme_for_group(self.group_name)
        bg_color = theme.get("theme_color", "#ffffff") if theme else "#ffffff"
        self.configure(bg=bg_color)

        # 👇 Replaced f-string with .format()
        tk.Label(self, text="{} Group Chat".format(self.group_name), font=("Arial", 16, "bold"), bg=bg_color).pack(pady=10)

        self.chat_frame = tk.Frame(self, bg=bg_color)
        self.chat_frame.pack(fill="both", expand=True)

        self.message_entry = tk.Entry(self)
        self.message_entry.pack(padx=10, pady=5, fill="x")
        self.message_entry.bind("<Return>", self.send_message)

        self.load_messages()

    def load_messages(self):
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        messages = load_group_messages(self.group_name)
        theme = get_theme_for_group(self.group_name)
        color = theme.get("theme_color", "#e1f5fe") if theme else "#e1f5fe"

        for msg in messages:
            bubble = ChatBubble(
                self.chat_frame,
                sender=msg["sender"],
                message=msg["message"],
                align="left" if msg["sender"] != self.current_user else "right",
                bg_color=color
            )
            bubble.pack(anchor="w" if msg["sender"] != self.current_user else "e", pady=2, padx=5)

    def send_message(self, event=None):
        text = self.message_entry.get().strip()
        if not text:
            return

        save_group_message(self.group_name, self.current_user, text)
        self.message_entry.delete(0, tk.END)
        self.load_messages()
