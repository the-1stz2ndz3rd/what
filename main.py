import tkinter as tk
from screens.login_screen import LoginScreen
from screens.signup_screen import SignupScreen
from screens.dashboard import DashboardScreen
from screens.group_chat import GroupChatScreen
from screens.private_chat import PrivateChatScreen
from screens.profile_screen import ProfileScreen
from screens.settings_screen import SettingsScreen

class HobbyHiveApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hobby Hive")
        self.geometry("800x600")
        self.resizable(False, False)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.user_data = {}           # Holds info like username, hobbies, etc.
        self.current_group_data = {}  # Used for group chat
        self.private_recipient = ""   # Used for private chat

        self.create_frames()

        self.show_frame("LoginScreen")

    def create_frames(self):
        for F in (LoginScreen, SignupScreen, DashboardScreen,
                  GroupChatScreen, PrivateChatScreen,
                  ProfileScreen, SettingsScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name, **kwargs):
        frame = self.frames[page_name]

        # Optional data to screens
        if page_name == "GroupChatScreen" and "group_data" in kwargs:
            self.current_group_data = kwargs["group_data"]
            frame.load_messages(self.current_group_data)
        elif page_name == "PrivateChatScreen" and "recipient" in kwargs:
            self.private_recipient = kwargs["recipient"]
            frame.load_messages(self.private_recipient)
        elif page_name == "ProfileScreen":
            frame.load_profile()
        elif page_name == "SettingsScreen":
            pass  # Nothing to pre-load yet

        frame.tkraise()

if __name__ == "__main__":
    app = HobbyHiveApp()
    app.mainloop()
