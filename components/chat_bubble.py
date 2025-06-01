import tkinter as tk

class ChatBubble(tk.Frame):
    def __init__(self, parent, sender, message, align="left", bg_color=None, **kwargs):
        super().__init__(parent, bg=bg_color or "#f0f0f0", **kwargs)

        bubble = tk.Frame(self, bg=bg_color or "#e1f5fe", bd=1, relief="solid", padx=5, pady=3)
        sender_label = tk.Label(bubble, text=sender, font=("Arial", 8, "bold"), bg=bubble["bg"])
        message_label = tk.Label(bubble, text=message, wraplength=300, justify="left", bg=bubble["bg"])

        sender_label.pack(anchor="w")
        message_label.pack(anchor="w")

        bubble.pack(side="left" if align == "left" else "right", padx=10, pady=5)
