"""A number-guessing game."""

import random
# Put your code here
# Greet the player

name = input("Please enter your name: ")
print (f'Hello {name}!')

#choose a random number

numbertoguess = random.randrange(1,100)
print(numbertoguess)

#repeat this part until random number equals the guess 
#ask player to input a number from 1-100

str_guess = input("Please choose a number between 1 and 100: ")
guess = int(str_guess)

#check if input number is equal to random number

if guess == numbertoguess:
    print(f'Congratulations {name}! You guessed the number!!!')

#increase number of guesses
#if random number is not equal to input number, is it higher?
#if random number is not equal to or higher, it must be lower
#give user a hint
#once random number equals the guess, congratulate the user.
