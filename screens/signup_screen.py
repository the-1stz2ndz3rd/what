# screens/signup_screen.py
import tkinter as tk
from tkinter import messagebox
from utils.auth import register_user

class SignupScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Signup", font=("Helvetica", 24)).pack(pady=20)
        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Hobbies (comma-separated)").pack()
        self.hobbies_entry = tk.Entry(self)
        self.hobbies_entry.pack()

        tk.Button(self, text="Create Account", command=self.attempt_signup).pack(pady=10)
        tk.Button(self, text="Back to Login", command=lambda: controller.show_frame("LoginScreen")).pack()

    def attempt_signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hobbies = [h.strip() for h in self.hobbies_entry.get().split(",") if h.strip()]

        if username and password and hobbies:
            if register_user(username, password, hobbies):
                messagebox.showinfo("Success", "Account created!")
                self.controller.show_frame("LoginScreen")
            else:
                messagebox.showerror("Error", "Username already exists.")
        else:
            messagebox.showerror("Error", "All fields are required.")
