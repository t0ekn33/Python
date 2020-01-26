
"""lab07_game.py

Make the operator guess the correct number between 1 and 100. The
program starts an infinite loop, tests explicitly for each possible
condition and prints all results within the loop.  A correct answer
causes a break to be issued to end the loop.
"""

from random import randrange
ran_num = randrange(1, 101)
attempts = 0
while True:
    temporary = input('Enter your guess: ')
    guess = int(temporary)
    attempts += 1   # shorthand for attempts = attempts + 1
    if guess < ran_num:
        print('Your guess is too low')
    elif guess > ran_num:
        print('Your guess is too high')
    else:
        print('Your guess is correct!')
        print('You succeeded in %d attempts.' % (attempts))  # Older formatting
        print('You succeeded in {0:d} attempts.'.format(attempts))
        break
