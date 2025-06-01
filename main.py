import tkinter as tk
from screens.login_screen import LoginScreen
from screens.signup_screen import SignupScreen
from screens.dashboard import Dashboard
from screens.group_chat import GroupChatScreen  # Future screens can be added
from utils.theme_loader import apply_background

class HobbyHiveApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hobby Hive")
        self.geometry("1000x700")
        self.resizable(False, False)

        # Dictionary to hold all frames
        self.frames = {}

        # Container to hold current screen
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Store active user (None at start)
        self.active_user = None

        # Initialize all the screens
        for F in (LoginScreen, SignupScreen, Dashboard, GroupChatScreen):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginScreen")

    def show_frame(self, screen_name):
        '''Raises the screen to the top'''
        frame = self.frames[screen_name]
        frame.tkraise()

    def set_active_user(self, user):
        '''Stores the logged-in user's info'''
        self.active_user = user

if __name__ == "__main__":
    app = HobbyHiveApp()
    app.mainloop()
