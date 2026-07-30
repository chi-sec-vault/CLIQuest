import os

USER_FILE = "data/user.txt"


def get_user_name():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return file.read()

    name = input("\nBefore we begin...\nWhat should I call you? ")

    # Ensure the 'data' folder exists before trying to save the user file
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(USER_FILE, "w") as file:
        file.write(name)

    return name
