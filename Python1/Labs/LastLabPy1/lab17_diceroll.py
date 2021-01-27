"""lab17_diceroll.py

This program simulates the rolling of a pair of dice a predetermined
number of times.  It counts the number of 2's and the number of 7's
rolled.  Then it calculates the percentage of rolls that were 7's or 2's
respectively.  It prints the results formatted to one decimal place using
both the old and new methods of formatting.
"""

from random import randrange
twos = 0
sevens = 0
counter = 10000
# counter = 10_000  # Python 3.6 or higher allows an underscore for readability
for i in range(counter):
    roll = randrange(1, 7) + randrange(1, 7)
    if roll == 2:
        twos += 1
    if roll == 7:
        sevens += 1

# The new way of formatting. The % sign takes the place of f. It performs
# the necessary multiplication by 100 and provides the trailing % sign.
print('Total rolls - {0:,d}'.format(counter))
print('{0:.1%} of the rolls were sevens'.format(sevens / counter))
print('{0:.1%} of the rolls were twos'.format(twos / counter))
print()
# The old way. The % sign has to be included and escaped in order to print.
per2 = 100.0 * twos / counter  # and the multiplications have to be done
per7 = 100.0 * sevens / counter  # explicitly
print('Total rolls - %s' % (format(counter, ',d')))
print('%.1f%% of the rolls were sevens' % (per7))
print('%.1f%% of the rolls were twos' % (per2))
