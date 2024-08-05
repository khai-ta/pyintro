while True:
    import random

    choices = ["rock", "paper", "scissors", "or"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("result: draw")
    elif player == "rock":
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("result: you win")
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("result: you lose")
    elif player == "paper":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("result: you win")
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("result: you lose")
    elif player == "scissors":
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("result: you win")
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("result: you lose")
    elif player == "or":
        print("computer:", computer)
        print("player:", player)
        print("result: you win")

    player = input("play again? (yes/no): ").lower()
    if player != "yes":
        break

print("thanks for playing!")


