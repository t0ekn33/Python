"""lab_03d_dup_dates_alt.py

This program generates 23 random integers in the range 1 to 365
inclusive.  Then it checks to see if any of these numbers, which
represent dates, are duplicates. It does this by using the index
method for each item in the list.
See exercise 10-8 on page 118 in **Think Python**
"""

from random import randrange
def has_duplicates(the_list):

    """ Checks given list for duplicates and returns True if so """

    for i in range(len(the_list)):
        if the_list.index(the_list[i]) != i: # Is this not the first occurrence?
            return True
    return False

same_birthday_counter = 0
trials = 100
for trial in range(trials):
    birthdays = []
    for b in range(23):
        birthdays.append(randrange(1, 366))
    if has_duplicates(birthdays):
        same_birthday_counter += 1
print("{0:d} sets of 23 people had the same birthday in {1:d} trials".format(
    same_birthday_counter, trials))



