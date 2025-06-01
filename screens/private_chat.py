import tkinter as tk
from tkinter import ttk
from utils.chat_manager import get_private_messages, add_private_message
from components.chat_bubble import ChatBubble
import datetime

class PrivateChatScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="white")

        self.recipient = None
        self.chat_frame = tk.Frame(self, bg="white")
        self.chat_frame.pack(expand=True, fill="both", padx=20, pady=10)

        # Scrollbar + Canvas setup for chat
        self.canvas = tk.Canvas(self.chat_frame, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.chat_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Message entry
        entry_frame = tk.Frame(self, bg="white")
        entry_frame.pack(fill="x", padx=20, pady=(0, 20))
        self.msg_entry = ttk.Entry(entry_frame)
        self.msg_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        send_btn = ttk.Button(entry_frame, text="Send", command=self.send_message)
        send_btn.pack(side="right")

        # Back button
        back_btn = ttk.Button(self, text="← Back", command=lambda: controller.show_frame("DashboardScreen"))
        back_btn.place(x=10, y=10)

    def load_chat(self):
        self.recipient = self.controller.private_recipient
        current_user = self.controller.current_user

        if not self.recipient:
            return

        # Clear previous messages
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        chat_key = self.get_chat_key(current_user, self.recipient)
        messages = load_private_chat(chat_key)

        for msg in messages:
            is_user = msg['sender'] == current_user
            bubble = ChatBubble(self.scrollable_frame, msg['text'], is_user)
            bubble.pack(anchor="e" if is_user else "w", pady=2, padx=5)

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def send_message(self):
        msg = self.msg_entry.get().strip()
        if not msg:
            return

        current_user = self.controller.current_user
        recipient = self.controller.private_recipient
        timestamp = datetime.datetime.now().isoformat(timespec='seconds')

        chat_key = self.get_chat_key(current_user, recipient)
        save_private_message(chat_key, current_user, msg, timestamp)

        bubble = ChatBubble(self.scrollable_frame, msg, is_user=True)
        bubble.pack(anchor="e", pady=2, padx=5)
        self.msg_entry.delete(0, tk.END)

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    @staticmethod
    def get_chat_key(user1, user2):
        return "_".join(sorted([user1, user2]))
