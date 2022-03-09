# This is 'Gues the number game'
import random

secretNumber = random.randint(1, 100)
print('Im thinking of a number between 1 and 100')

#ask the player to guess 6 times
for guessesTaken in range (1, 100):
    print('Take a guess')
    guess = random.randint(1, 100)

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is to high')
    else:
        break #This is a correct answer
if guess == secretNumber:
    print('Good job, you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))