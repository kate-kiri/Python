
# Number Guessing Game
import random

lowest_number = 1
high_number = 50

answer = random.randint(lowest_number,  high_number)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"\nSelect a Number between {lowest_number} and { high_number}:")

while is_running:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Enter a number!")
        continue

    guess = int(guess)
    guesses += 1

    if guess < lowest_number or guess >  high_number:
        print("Your guess is out of range!")
        print(f"Select a Number between {lowest_number} and { high_number}:")

    elif guess < answer:
        print("TOO LOW!")

    elif guess > answer:
        print("TOO HIGH!")

    else:
        print(f"CORRECT! Your answer was {answer}")
        print(f"Your guesses were {guesses}") 
        is_running = False

