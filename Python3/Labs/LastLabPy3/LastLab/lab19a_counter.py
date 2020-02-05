"""lab19a_counter.py

This program counts the number of times each character (except whitespace)
is used in the book, "Alice in Wonderland."  It is an example of using
the translate method in conjunction with the maketrans function.  In this
case maketrans is used to create a dictionary with only whitespace
characters to delete.  Translate is used to delete the whitespace.  Then,
the Counter class (imported from collections) is instantiated with the
translated book as input.  After that, the most_common method is used to
print the top 20 characters.
"""

from string import whitespace
from collections import Counter

# with open('/home/student/pydata/alice_in_wonderland.dat', 'r') as fin:
with open('c:/pydata/alice_in_wonderland.dat', 'r') as fin:
    bookin = fin.read().upper()

# Use translate just to remove white space.
trbookin = bookin.translate(str.maketrans('', '', whitespace))
x = Counter(trbookin) # instantiate Counter with the book as input
# print the 20 most common letters in the book
for i, j in x.most_common(20):
    print('{0} {1:6,d}'.format(i, j))
print('Total non whitespace characters - {0:,d}'.format(
    sum(x.values())))
