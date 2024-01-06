import random


def guess(x):
    random_number = random.randint(1, x)
    your_guess = 0

    while your_guess != random_number:
        your_guess = int(input(f"Guess a random between 1 and {x}: "))
        if your_guess > random_number:
            print(f"Sorry, guess again. Number is too high.")
        elif your_guess < random_number:
            print(f"Sorry, guess again. Number is too low")

    print(f"You have guessed the correct number!")


guess(10)
