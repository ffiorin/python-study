# This is a guess the number game - Udemy | Automate the Boring Stuff with Python Programming | 12. Writing a "Guess the Number" Program
import random
print("Welcome to the Guess the Number Game! What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 10. You have 4 attempts to guess it.")
secretNumber = random.randint(1, 10)

for guessesTaken in range(1, 5):  # The player has 4 attempts to guess the number
    print("Take a guess.")
    try:
        guess = int(input())

        if not 1 <= guess <= 10:
            print("Please enter a number from 1 to 10.")
            continue

        if guess < secretNumber:
            print("Your guess is too low. Try again! You have " + str(4 - guessesTaken) + " guesses left.")
        elif guess > secretNumber:
            print("Your guess is too high. Try again! You have " + str(4 - guessesTaken) + " guesses left.")
        else:
            break  # This condition is the correct guess!
    
    except ValueError: # Handles the case where the user inputs a non-integer value, like letters or symbols
        print("Error: Please enter a valid number from 1 to 10.")
        continue

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Failed! The number I was thinking of was " + str(secretNumber) + ".")