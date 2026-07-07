import os

print("Welcome to CLIQuest!")

if os.path.exists("user.txt"):
    with open("user.txt", "r") as file:
        name = file.read()

    print(f"\n👋 Welcome back, {name}!")
    print("Ready to conquer today's commands? 🚀")

else:
    name = input("\nBefore we begin...\nWhat should I call you? ")

    with open("user.txt", "w") as file:
        file.write(name)

    print(f"\n👋 Welcome {name}! Excited to start this journey with you.")
    print("Ready to conquer these commands? 🚀")
