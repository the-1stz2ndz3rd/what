# screens/dashboard.py
import tkinter as tk
from tkinter import Scrollbar, Canvas, Frame
import json
from components.group_card import GroupCard
from utils.file_handler import load_json
from utils.theme_loader import apply_theme

class DashboardScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.bg_image = tk.PhotoImage(file="assets/backgrounds/dashboard_bg.jpg")
        
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        title = tk.Label(self, text="Hobby Hive Groups", font=("Helvetica", 18, "bold"), bg="#ffffff")
        title.pack(pady=10)

        self.canvas = Canvas(self, bg="white", highlightthickness=0)
        scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = Frame(self.canvas, bg="white")

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.load_groups()

    def load_groups(self):
        groups_data = load_json("data/groups.json")
        for hobby_name, group_info in groups_data.items():
            card = GroupCard(self.scroll_frame, group_info, self.open_group_chat)
            card.pack(fill='x', padx=20, pady=5)

    def open_group_chat(self, group_name):
        self.controller.show_frame("GroupChatScreen", group_name=group_name)
