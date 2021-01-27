"""lab07_game_alt.py

Make the operator guess the correct number between 1 and 100. A correct
guess causes the while loop to exit.  Then the results are printed
outside the loop.
"""

from random import randrange
ran_num = randrange(1, 101)
attempts = 0
guess = 0  # Initialize the guess with an incorrect number
while guess != ran_num:
    temporary = input('Enter your guess: ')
    guess = int(temporary)
    attempts += 1   # shorthand for attempts = attempts + 1
    if guess < ran_num:
        print('Your guess is too low')
    elif guess > ran_num:
        print('Your guess is too high')

print('Your guess is correct!')
print('You succeeded in %d attempts.' % (attempts))  # Older formatting
print('You succeeded in {0:d} attempts.'.format(attempts))
print(f'You succeeded in {attempts:d} attempts.')  # Using an f-string
print('You succeeded in', attempts, 'attempts')  # Didn't need formatting
