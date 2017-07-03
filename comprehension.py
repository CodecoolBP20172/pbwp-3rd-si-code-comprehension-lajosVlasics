#It is a number guessing game. The computer will think of a random number from 1 to 20, and ask you to guess it. The computer will tell you if each guess is too high or too low. You win if you can guess the number within six tries.

import random  # Import random module

guessesTaken = 0  # Assign a starting 0 value to this variable

print('Hello! What is your name?')  # Printing out 'Hello! What is your name?' string
myName = input()  # Assign the user input (users name) to this variable

number = random.randint(1, 20)  # Assign a randomly picked number between 1-20 to this variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Concatenate a string with myName variable and print it

while guessesTaken < 6:  # Runs a loop until guessesTaken value is lower then 6
    print('Take a guess.')  # print a string
    guess = input()  # Assign the user input (the guessed number) to this variable
    guess = int(guess)  # Convert this string variabe to an integer variable

    guessesTaken += 1  # Add 1 to this variable

    if guess < number:  # Check if the guess variable is less then the number variable
        print('Your guess is too low.')  # Print a messege if the previous condition is true

    if guess > number:  # Check if the guess variable is more then the number variable
        print('Your guess is too high.')  # Print a messege if the previous condition is true

    if guess == number:  # Check if the guess variable equals to the the number variable
        break  # Stops running the loop if the previous condition is true

if guess == number:  # Check if the guess variable equals to the number variable
    guessesTaken = str(guessesTaken)  # Convert guessesTaken integer to string variable
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Concatenate a string with myName and guesseTaken variables and print it out

if guess != number:  # Check if the guess variable not equals to the number variable
    number = str(number)  # Convert number integer to string variable
    print('Nope. The number I was thinking of was ' + number)  # Concatenate a string with number variable and print it out
