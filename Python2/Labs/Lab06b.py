"""LAB 06b
Redo lab 03d in which you determined the probability of two or
more people in a group of 23 had the same birthday. This time,
create an empty set() and place each random number you generate
in the set using the add method. What happens to the duplicates?
How does this help you determine if there were duplicates?
My version of lab 03d is available online.

"""
from random import randrange
randSet = set()

same_birthday_counter = 0
trials = 100
for trial in range(trials):
    birthdays = [] #create 100 empty lists
    for cntr in range(23):
        birthdays.append(randrange(1, 366)) #adds 23 people's random days to each list
        randSet.add(randrange(1,366))
    for day in birthdays: 
        if birthdays.count(day) > 1:
            same_birthday_counter += 1
            break  # avoids counting multiple occurances (3 or more duplicates)
print("{0:,d} sets of 23 people had the same birthday in {1:,d} trials".format(
    same_birthday_counter, trials))
print(randSet)
