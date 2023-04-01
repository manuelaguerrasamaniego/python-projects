import random


def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0

    while user_guess != random_number:
        user_guess = int(input(f"Enter a number between 1 and {x}: "))
        if user_guess < random_number:
            print(f"Sorry, {user_guess} is too low... ")
        elif user_guess > random_number:
            print(f"Sorry, {user_guess} is too high...")

    right = f"Congrats! {user_guess} is the right number! "

    return right


print(guess(100))
