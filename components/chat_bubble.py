import tkinter as tk

class ChatBubble(tk.Frame):
    def __init__(self, parent, sender, message, is_self=False):
        super().__init__(parent, bg="white", padx=5, pady=2)

        bubble_color = "#DCF8C6" if is_self else "#FFFFFF"
        align = "e" if is_self else "w"
        anchor = "e" if is_self else "w"

        frame = tk.Frame(self, bg=bubble_color, bd=1, relief="solid")
        frame.pack(anchor=anchor, padx=10, pady=2, fill="x")

        name_label = tk.Label(frame, text=sender, font=("Helvetica", 9, "bold"), bg=bubble_color, anchor=align)
        name_label.pack(anchor=anchor)

        message_label = tk.Label(frame, text=message, wraplength=300, justify="left", bg=bubble_color, anchor=align)
        message_label.pack(anchor=anchor)
