# Number Guessing Game

import random

guesses_done = 0
difficulty = 0

print("Number Guessing Game")
print("You are to guess the number randomly chosen by me within any level")
print("There are 3 levels:")
print("Easy")
print("Medium")
print("Hard")

while True:
    level = input("Choose a level:\n")

    if level == "Easy":
        difficulty = 10
        guesses_allowed = 6
        break

    if level == "Medium":
        difficulty = 20
        guesses_allowed = 4
        break

    if level == "Hard":
        difficulty = 50
        guesses_allowed = 3
        break

random_number = random.randint(1, difficulty)
# print(random_number)

while guesses_done < guesses_allowed:
    guess = input("Guess the number between 1 and {}:".format(difficulty))
    guess = int(guess)
    guesses_done = guesses_done + 1
    guesses_left = guesses_allowed - guesses_done

    if guess == random_number:
        print("You got it right!")
        break
    else:
        print("That was wrong")
        print("You have {} guesses left.".format(guesses_left))

    if guesses_done == guesses_allowed and guess != random_number:
        print("Game Over!")
