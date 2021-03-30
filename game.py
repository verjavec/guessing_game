"""A number-guessing game."""

import random
# Put your code here
# Greet the player

name = input("Please enter your name: ")
print (f'Hello {name}!')

#choose a random number

numbertoguess = random.randrange(1,100)
print(numbertoguess)
keep_guessing = True
num_guesses = 0

#repeat this part until random number equals the guess 
#ask player to input a number from 1-100


#check if input number is equal to random number
while keep_guessing:
    str_guess = input("Please choose a number between 1 and 100: ")
    guess = int(str_guess)

    if guess == numbertoguess:
        num_guesses += 1
        print(f'Congratulations {name}! You guessed the number in {num_guesses} tries!!!')

    #increase number of guesses
        keep_guessing = False

    #if random number is not equal to input number, is it higher?
    elif guess > numbertoguess:
        print(f'Too high! Try a lower number, {name}.')
        num_guesses += 1
        

    elif guess < numbertoguess:
        print(f'Too low! Try a higher number, {name}.')
        num_guesses += 1
        
    #if random number is not equal to or higher, it must be lower
    #give user a hint
    #once random number equals the guess, congratulate the user.
