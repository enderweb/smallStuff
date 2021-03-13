def all():
    import random
    print("Welcome to rock, paper scissors.")
    userChoice = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n"))
    computerChoice = random.randint(1, 3)


    #user stuff
    if userChoice == 1:
        userItem = "Rock"
    elif userChoice == 2:
        userItem = "Paper"
    elif userChoice == 3:
        userItem = "Scissors"
    else:
        print("There has been an error")


    #computer stuff
    if computerChoice == 1:
        computerItem = "Rock"
    elif computerChoice == 2:
        computerItem = "Paper"
    elif computerChoice == 3:
        computerItem = "Scissors"

    #fin

    print(f"You picked {userItem}")
    print(f"The computer picked {computerItem}")
    if userChoice == computerChoice:
        print("You tied :/")
    if userChoice == 1 and computerChoice == 2:
        print("You lost D:")
    if userChoice == 1 and computerChoice == 3:
        print("You win :D")
    if userChoice == 2 and computerChoice == 1:
        print("You win :D")
    if userChoice == 2 and computerChoice == 3:
        print("You lost D:")
    if userChoice == 3 and computerChoice == 1:
        print("You lost D:")
    if userChoice == 3 and computerChoice == 2:
        print("You win :D")
    playAgain = int(input("Would you like to play again?\n1 - Yes\n2 - No\n"))
    if playAgain == 1:
        all()
    else:
        print("Okay, have a nice day")
all()
