from utils.file_handler import read_json, write_json

def validate_login(username, password):
    users = read_json("data/users.json")
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def validate_signup(username, password, hobbies):
    if not username or not password:
        return False, "Username and password cannot be empty."

    users = read_json("data/users.json")
    for user in users:
        if user["username"] == username:
            return False, "Username already exists."

    users.append({
        "username": username,
        "password": password,
        "hobbies": hobbies
    })
    write_json("data/users.json", users)
    return True, "Signup successful."
