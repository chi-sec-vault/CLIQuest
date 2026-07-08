def whoami_lesson():

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🧭 Quest 1 - Who Am I?")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print("\nImagine you've just logged into a Linux machine.")
    print("Before doing anything...")
    print("Wouldn't you like to know who Linux thinks you are?")

    input("\nPress Enter to continue...")

    guess = input("\n💭 What command do you think shows your current username?\n> ")

    if guess.lower() == "whoami":
        print("\n🎉 Nice! You got it right.")
    else:
        print("\n😊 Good guess!")
        print("The command we're looking for is: whoami")

    print("\n📖 What does it do?")
    print("It displays the username of the current logged-in user.")

    print("\n💻 Open another terminal and run:")
    print("whoami")

    input("\nPress Enter after you've tried it...")

    print("\n🎉 Quest Complete!")
    print("You learned:")
    print("✅ whoami")
    print("\n⭐ +10 XP (XP system coming soon!)")
