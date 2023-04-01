import random


def rockpaperscissors():
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    human = input("What's your choice (rock, paper, scissors)? ")

    if (computer == 'rock' and human == 'paper') or (computer == 'paper' and human == 'scissors') or (computer == 'scissors' and human == 'rock'):
        print("Congrats! You win! ")
    elif computer == human:
        print("It's a tie! ")
    else:
        print("You lose! ")

    print(f"Computer's choice: {computer} ")
    print(f"Your choice: {human} ")
    play_again = input("Play again? (y/n) ")

    if play_again.lower() == 'y':
        rockpaperscissors()


rockpaperscissors()
