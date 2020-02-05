"""Lab 19b
Alternatively, use translate and split to isolate each word in
the book. Then use Counter and other tools such as sets to
count the total words in the book, the unique words in the
book, the number of words in the book that are not in
words.txt and the top 20 words in the book by use counts.
(See answers on the next slide)

"""

from string import punctuation
from collections import Counter

fin = open("Python3/Labs/alice_in_wonderland.dat", "r")
for word in fin:
bookin = fin.read().lower().strip()  # read in the entire book and lower the case
# bookin = bookin.translate(str.maketrans('', '', " ")) # Remove whitespace

# print(bookin)
cwords = Counter(bookin)
print(cwords.most_common(20))