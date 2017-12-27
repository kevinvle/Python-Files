# guess the number
import random

print ('Hello. what is your name?')
name = input()

print('Well, ' + name +' I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess. ')
    guess = int(input()) # Input gets converted to string --> must convert to int

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:            # guess == secretNumber:
        break
    
if guess == secretNumber:
    print('good job.' + name + ' you did it in' + str(guessesTaken) + ' guesses')
else:
    print (' bad job. the right answer is ' + str(secretNumber) + ' ' )
   




