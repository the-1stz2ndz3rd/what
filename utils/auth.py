import hashlib
from utils.file_handler import read_json, write_json

USER_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_signup(username, password, confirm_password):
    if not username or not password:
        return False, "Username and password cannot be empty."
    if password != confirm_password:
        return False, "Passwords do not match."
    if len(password) < 5:
        return False, "Password must be at least 5 characters."
    
    users = read_json(USER_FILE)
    for user in users:
        if user["username"] == username:
            return False, "Username already exists."
    
    return True, "Valid"

def signup_user(username, password):
    users = read_json(USER_FILE)
    users.append({
        "username": username,
        "password": hash_password(password),
        "hobbies": [],  # filled later from selected groups
        "profile": {}
    })
    write_json(USER_FILE, users)

def login_user(username, password):
    users = read_json(USER_FILE)
    for user in users:
        if user["username"] == username and user["password"] == hash_password(password):
            return True
    return False
