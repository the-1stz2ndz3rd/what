import tkinter as tk
from tkinter import ttk
from utils.chat_manager import get_private_messages, send_private_message
from components.chat_bubble import ChatBubble

class PrivateChatScreen(tk.Frame):
    def __init__(self, master, controller, current_user, other_user):
        super().__init__(master)
        self.controller = controller
        self.current_user = current_user
        self.other_user = other_user

        self.canvas = tk.Canvas(self, bg="#ffffff", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.chat_frame = tk.Frame(self.canvas, bg="#ffffff")
        self.chat_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(fill="x", side="left", expand=True, padx=10, pady=5)
        self.entry.bind("<Return>", self.send_message)

        self.send_btn = tk.Button(self, text="Send", command=self.send_message)
        self.send_btn.pack(side="right", padx=10, pady=5)

        self.load_messages()

    def load_messages(self):
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        messages = get_private_messages(self.current_user, self.other_user)
        for msg in messages:
            ChatBubble(self.chat_frame, msg["sender"], msg["text"]).pack(anchor="w" if msg["sender"] != self.current_user else "e", pady=2, padx=5)

    def send_message(self, event=None):
        text = self.entry.get().strip()
        if text:
            send_private_message(self.current_user, self.other_user, self.current_user, text)
            self.entry.delete(0, tk.END)
            self.load_messages()
