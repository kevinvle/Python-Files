#This is a guessing game
import random

print('Hello. What is your name?')
name = input()

print('well ' + name + " I am thinking of a # from 1-20")
secretNumber = random.randint(1, 20)

print(' DEBUG SECRET # is ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print ('your guess is too high.')
    else:
        break #This condition is for the correct guess!

if guess == secretNumber:
    print('congrats, you guessed my number in ' + str(guessesTaken) + ' times')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) )

print('You took ' + str(guessesTaken) + ' guesses.')
