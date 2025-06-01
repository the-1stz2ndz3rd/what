# utils/matchmaker.py

def get_matches(current_user, all_users):
    """Return list of users who share at least one hobby with current_user"""
    current_hobbies = set(current_user.get("hobbies", []))
    matches = []

    for user in all_users:
        if user["username"] == current_user["username"]:
            continue  # skip self
        shared = current_hobbies.intersection(user.get("hobbies", []))
        if shared:
            matches.append({
                "username": user["username"],
                "shared_hobbies": list(shared)
            })

    return matches
