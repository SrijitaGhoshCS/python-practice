# Program 30: Number Guessing Game
import random
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100")
while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right:", secret_number)
        break
#variation:
import random

secret_number = random.randint(1, 50)
attempts = 5

print("Guess the number between 1 and 50. You have", attempts, "chances.")

for i in range(attempts):
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("🎉 Correct! The number was", secret_number)
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("Sorry, you're out of chances. The number was", secret_number)
