import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input(f"rock, paper or scissors?: ").lower()

    if player == computer:
        print(f"Computer: {computer}")
        print(f"player: {player}")
        print("Tie! ")
    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Loose!  ")
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Win!  ")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Loose!  ")
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Win!  ")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Loose!  ")
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("You Win!  ")

    play_again  = input(f"Do you want to play again? (Yes/no): ").lower()

    if play_again != "yes":
        break

print("Game Over! ")





