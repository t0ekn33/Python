"""LAB 06a
Read the book, "Alice in Wonderland" into memory. Create a
dictionary counting all the printable characters excluding
whitespace. Be sure not to count upper- and lower-case letters
separately. Creating the dictionary is the most important part
of this lab. When done, print the top 30 most frequently
occurring characters along with the number of occurrences.
If you have time, print five character/occurrences combinations
per line. Make sure all the elements of the printed lines form
neat columns.
"""
from string import whitespace

bookDict = dict()

fin = open('Python2/Labs/alice_in_wonderland.dat', 'r')
bookin = fin.read()

bookin = bookin.upper()
for char in bookin:
    if char is whitespace:
        continue
    elif char in bookin:
        bookin[char] += 1
    else:
        bookin[char] = 1

"""

if bookin.isprintable:
    if bookin.isspace:
        for c in bookin:
            if c in bookDict:
                bookDict[c] = bookDict[c] + 1
            else:
                bookDict[c] = 1
print(bookDict)
"""