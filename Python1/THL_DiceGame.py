"""
Tony Salazar
14JAN2020
Create a program that calls a function that simulates the rolling of a pair of dice.
Use randrange from the random module to accomplish this. Your main program
will deal with the total of the two dice.
• The rules are as follows:
• On the first roll, a total of 7 or 11 is an automatic win
• On the first roll, a total of 2, 3 or 12 is an automatic loss
• Any other number is called the Point. You must roll again. On subsequent rolls
the rules are as follows:
• You roll a 7 which is a loss.
• You roll the Point number again which is a win.
• Any other roll has no meaning and another roll is required.
• You start with $100 and bet $10 on each play.
• Print all the rolls and whether you have won or lost on one line.
• Print the funds balance and a request to play again on the next line. A ‘y’ or ‘Y’
means play again. Anything else ends play. A balance of $0 ends play
automatically.
"""
from random import randrange as rr

def roll_dice():
    roll = rr(1,7) + rr(1,7)
    return(roll)

ans = 'y'
bal = 100
cnt = 0

print("Starting balance: $", bal, sep = '')

while ans == 'y' or ans == 'Y':
    # Check for cash
    if bal <= 0:
        print("You are broke, goodbye!")
        break
    # First role of the dice
    roll1 = roll_dice()
    bal -= 10   #Place your bet
    print("First roll:", roll1)
    cnt += 1
    # 7 or 11 on first roll wins
    if roll1 == 7 or roll1 == 11:
        print("Winner!")
        bal += 20
        print("Balance: $", bal, sep = '')
        ans = input("Play again? y/n:")
    # 2, 3, or 12 on first roll loses
    elif roll1 == 2 or roll1 == 3 or roll1 == 12:
        print("You lose!")
        print("Balance: $", bal, sep = '')
        ans = input("Play again? y/n:")
    else:
        point = roll1   # Set game point
        print("Point:", point)
        # Roll dice until 7 or point 
        roll = roll_dice() 
        print(roll, end = ' ')
        while True:
            # Roll point wins
            if roll == point:
                print("Winner!")
                bal += 20
                print("Balance: $", bal, sep = '')
                ans = input("Play again? y/n:")
                break
            # Roll 7 loses
            elif roll == 7:
                print("You lose!")
                print("Balance: $", bal, sep = '')
                ans = input("Play again? y/n:")
                break
            else:
                roll = roll_dice()
                print(roll, end = ' ')
print("Number of plays:", cnt)
print("Ending balance: $", bal, sep = '')