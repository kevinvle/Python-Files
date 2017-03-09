# This is a guess the number game part 2

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20) # Give a number between 1 and 20 including 1 and 20. Stored in var called secret number

print('secret is' + str(secretNumber))
for guessesTaken in range(1, 7):
    print('take a guess.')
    guess = int(input()) # because their guess is a string
    
    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #correct guess

if guess == secretNumber:
    print('good job' + name + 'you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print(' Nope the number i was thinking of was ' + str(secretNumber))



print(' You took ' + str(guessesTaken) + ' guesses.')
