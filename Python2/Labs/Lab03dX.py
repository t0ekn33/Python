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
dupDay = [] 

from random import randrange 
def day():
    return randrange(1,366)

for cnt in range (1, 100):
    dupDay = day()
    for d in dupDay:
        if d == dupDay:
            print(dupDay[d])
