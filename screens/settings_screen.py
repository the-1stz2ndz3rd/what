from tkinter import Frame, Label, Button, BooleanVar, Checkbutton, messagebox
from utils.theme_loader import apply_theme

class SettingsScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.dark_mode = BooleanVar(value=False)
        self.build_ui()

    def build_ui(self):
        Label(self, text="⚙️ Settings", font=("Helvetica", 16)).pack(pady=10)

        Checkbutton(self, text="🌙 Enable Dark Mode", variable=self.dark_mode, command=self.toggle_dark_mode).pack(pady=5)

        Button(self, text="❓ Help / About", command=self.show_help).pack(pady=5)

    def toggle_dark_mode(self):
        mode = "dark" if self.dark_mode.get() else "light"
        apply_theme(self, mode)
        messagebox.showinfo("Theme Updated", f"Switched to {mode} mode!")

    def show_help(self):
        messagebox.showinfo("About Hobby Hive", 
            "📱 Hobby Hive v1.0\n\nAn app for AAU students to connect via hobbies.\n\nFeatures:\n• Group Chat\n• Private Chat\n• Hobby Matching\n• Events and More!\n\nCreated as a student project."
        )
