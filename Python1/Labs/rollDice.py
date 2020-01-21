from random import randrange as rr

def roll_dice():
    roll = rr(1,7) + rr(1,7)
    print(roll)

roll1 = roll_dice
print(roll1)
