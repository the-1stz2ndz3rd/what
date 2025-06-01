import tkinter as tk
from tkinter import ttk
from utils.file_handler import read_json
from components.group_card import create_group_card  # ✅ Correct import

class DashboardScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='white')

        title = tk.Label(self, text="Hobby Hive Dashboard", font=('Arial', 20, 'bold'), bg='white')
        title.pack(pady=20)

        self.group_frame = tk.Frame(self, bg='white')
        self.group_frame.pack(fill='both', expand=True)

        self.load_groups()

    def load_groups(self):
        groups = read_json('data/groups.json')

        for widget in self.group_frame.winfo_children():
            widget.destroy()

        for group in groups:
            card = create_group_card(self.group_frame, group, self.open_group_chat)
            card.pack(padx=10, pady=5, fill='x')

    def open_group_chat(self, group_data):
        group_name = group_data.get("group_name", "")
        self.controller.show_frame("GroupChatScreen", group_name=group_name)
