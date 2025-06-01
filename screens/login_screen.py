# screens/login_screen.py
import tkinter as tk
from tkinter import messagebox
from utils.auth import validate_login

class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Login", font=("Helvetica", 24)).pack(pady=20)
        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.attempt_login).pack(pady=10)
        tk.Button(self, text="Go to Signup", command=lambda: controller.show_frame("SignupScreen")).pack()

    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if validate_login(username, password):
            self.controller.show_frame("Dashboard")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
