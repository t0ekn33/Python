"""
Create a game.  Have the computer select a random integer between
1 and 100 inclusive. Then, have the operator take successive guesses
until they guess the correct number.  At each try, advise them
whether the guess is too high or too low.
If the guess is correct, tell them they won and tell them the
number of attempts they took.
Use the same format as the output sample to
the right.
This exercise requires you to use everything we have learned so far.
"""

from random import randrange

rand_num = randrange(1,100)
print(rand_num)


guess = input('1st: Guess a number between 1-100: ')
guess = int(guess)
cnt = 1
if(guess < rand_num):
    print('Too low!')
elif(guess > rand_num):
    print('Too high!')
else:
    print('Correct, and it only took you ', cnt, 'guesses!')
while(guess != rand_num):
    guess = input('loop: Guess a number between 1-100: ')
    guess = int(guess)
    if(guess < rand_num):
        print('Too low!')
    elif(guess > rand_num):
        print('Too high!')
    else:
        print('Correct, and it only took you ', cnt, 'guesses!')
        break
    cnt += 1
    print('Guesses: ', cnt)

 
