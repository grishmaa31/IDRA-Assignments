import random

secret = random.randint(1, 100)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1

    if attempts > 0:
        print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"Game Over! The correct number was {secret}.")
