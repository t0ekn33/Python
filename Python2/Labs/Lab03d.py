"""LAB 03d
From exercise 10-8 in the book, "Think Python":
If there are 23 students in your class, what are the chances that two
of you have the same birthday? You can estimate this probability by
generating random samples of 23 birthdays and checking for
matches.
Write the program such that you run the exercise at least 100 times.
At the conclusion of the program print the number of times duplicate
dates were detected. Use the randrange function in the random
module to generate numbers from 1 to 365 to simulate dates. Use
the count method to determine whether there are duplicates.
Mathematically, the probability of duplicates occurring is about 50%.
Your results should be in the area of 40% to 60%. 
"""

from random import randrange 

def rand_day():
    rando = randrange(1, 366)
    return(rando)

tests = 100
same_day = 0 
for test in range(tests):
    bday = []
    #print(test) # 1-100
    for cnt in range(23):
        bday.append(randrange(1, 366))
        #bday.append(rand_day)
    for day in bday:
        if bday.count(day) > 1:
            same_day += 1
            break 
        
print("{0:d} sets of 23 people had the same bday in {1:,d} trials.".format(same_day, tests))


