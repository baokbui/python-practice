import random

guesses = 0
stop = ""

while stop != "exit":
    number = random.randint(1,9)
    guess = int(input("Guess a number from 1-9: "))
    guesses += 1

    if number == guess:
        print("Congrats you guessed the number!")
        print(f"Your number: {guess}   Actual number: {number}")
    elif guess > 9 or guess < 1:
        print("Your number is not in the range of 1 and 9")
    else:
        print("Unfortunately your guess was wrong.")
        print(f"Your number: {guess}   Actual number: {number}")

    stop = input("Would you like to continue? Press enter to continue or type 'exit' to quit: ")

print("Thanks for playing!")