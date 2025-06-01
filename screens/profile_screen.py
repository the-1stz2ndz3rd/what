from tkinter import Frame, Label, Button, Checkbutton, IntVar, Toplevel, messagebox
from utils.file_handler import load_json, save_json
from utils.matchmaker import get_matches

class ProfileScreen(Frame):
    def __init__(self, parent, controller, current_user):
        super().__init__(parent)
        self.controller = controller
        self.current_user = current_user
        self.hobby_vars = {}
        self.hobbies = [
            "Photography", "Philosophy", "Singing", "Playing Musical Instruments",
            "Acting", "Crocheting", "Reading", "Hiking", "Running", "Dance",
            "Football (Soccer)", "Basketball", "Skateboarding", "Video Gaming",
            "Coding/Programming", "Learning Languages", "Traveling", "Astronomy",
            "Weight Lifting", "Martial Arts", "Fashion Design", "Drawing",
            "Cooking", "Watching Movies", "Social Media Content Creating"
        ]
        self.build_ui()

    def build_ui(self):
        Label(self, text=f"Profile: {self.current_user}", font=("Helvetica", 16)).pack(pady=10)
        Label(self, text="Select Your Hobbies:", font=("Helvetica", 12)).pack()

        # Load user data
        users = load_json("data/users.json")
        user_info = next((u for u in users if u["username"] == self.current_user), {})
        selected_hobbies = user_info.get("hobbies", [])

        for hobby in self.hobbies:
            var = IntVar(value=1 if hobby in selected_hobbies else 0)
            self.hobby_vars[hobby] = var
            Checkbutton(self, text=hobby, variable=var).pack(anchor="w")

        Button(self, text="💾 Save Changes", command=self.save_hobbies).pack(pady=10)
        Button(self, text="💡 View Hobby Matches", command=self.show_matches).pack(pady=5)

    def save_hobbies(self):
        selected = [h for h, v in self.hobby_vars.items() if v.get() == 1]
        users = load_json("data/users.json")
        for user in users:
            if user["username"] == self.current_user:
                user["hobbies"] = selected
        save_json("data/users.json", users)
        messagebox.showinfo("Saved", "Your hobbies have been updated.")

    def show_matches(self):
        matches = get_matches(self.current_user)
        match_text = "\n".join(matches) if matches else "No hobby matches found."
        popup = Toplevel(self)
        popup.title("Recommended Matches")
        Label(popup, text="Users with similar hobbies:", font=("Helvetica", 12)).pack(pady=10)
        Label(popup, text=match_text, justify="left").pack(padx=10, pady=5)
