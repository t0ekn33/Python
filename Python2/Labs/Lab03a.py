"""
Lab 3a – Probability
Plan and execute the following program.
Simulate the rolling of a pair of dice 100,000
times accumulating the results of each roll in
a list (e.g., the number of two's, the number
of three's and so on). When finished, print
the percentage of times each possible roll
occurred. Visually compare your results to
the mathematically derived results in the
adjacent table.
How many elements will there be? How will
you initialize your list? What will you use for
an index?
"""
from random import randrange as rr
x = 0 
i = 2
avg = 0
table = 13 * [0] #create empty table with 14 cells

def roll_dice():
    roll = rr(1,7) + rr(1,7)
    return(roll)


while x < 100000:
    roll = roll_dice()
    table[roll] += 1 #add 1 to the table sub roll
    x +=1 
print(table)
while i <= 12:
    avg = table[i] / x  #calculate avg
    print(i, '{0:.2%}'.format(avg)) 
    i += 1