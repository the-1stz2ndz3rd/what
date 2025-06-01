import tkinter as tk

class UserCard(tk.Frame):
    def __init__(self, parent, username, hobbies, on_click):
        super().__init__(parent, bd=2, relief="groove", padx=8, pady=5, bg="#f0f0f0")

        self.username = username
        self.on_click = on_click

        tk.Label(self, text=username, font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w")
        tk.Label(self, text=", ".join(hobbies), font=("Helvetica", 10), fg="gray", bg="#f0f0f0").pack(anchor="w")

        self.bind("<Button-1>", self.clicked)
        for widget in self.winfo_children():
            widget.bind("<Button-1>", self.clicked)

    def clicked(self, event):
        self.on_click(self.username)
