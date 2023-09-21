import random


number_to_be_guessed = random.randint(1, 10)

number_of_guesses = 0

while number_of_guesses < 5:

    number = int(input("Enter a number:"))
    if number_to_be_guessed != number:
        print("You are Wrong, Try Again")
    else:
        print("Correct")
        break
    number_of_guesses += 1
print('Game Over')
