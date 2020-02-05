"""Lab 19
a) Use the file alice_in_wonderland.dat to create a Counter.
First, read the entire document into memory, and remove all
whitespace using translate/maketrans. Then, use a Counter to
determine the 20 most used characters in this document.
Print out each character and its number of occurrences in
descending order by use count. Be sure to make all cases the
same
"""
from string import whitespace
from collections import Counter

fin = open("Python3/Labs/alice_in_wonderland.dat", "r")
bookin = fin.read().lower()  # read in the entire book and lower the case
bookin = bookin.translate(str.maketrans('', '', whitespace )) # Remove whitespace

cwords = Counter(bookin)
print(cwords.most_common(20))