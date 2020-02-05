"""lab19b_counter.py

This program creates a set out of word.txt which is a collection of English
language words.  Then it reads the book, lowers all the text, replaces all
punctuation except apostrophes with spaces, removes all apostrophes and 
splits on whitespace processing the result with an instantiation of Counter.
"""

from collections import Counter
from string import punctuation

#with open('/home/student/pydata/words.txt') as fin:
with open('c:/pydata/words.txt') as fin:
    eng_set = set(fin.read().splitlines())

#with open('/home/student/pydata/alice_in_wonderland.dat') as fin:
with open('c:/pydata/alice_in_wonderland.dat') as fin:
    bookin = fin.read().lower()

remove_chr = punctuation.replace("'", "") # Not really necessary
bookin = bookin.translate(str.maketrans(
                            remove_chr, len(remove_chr) * ' ', "'"))
book_words = Counter(bookin.split())
print('Total words in book -', sum(book_words.values())) 
print('Unique words in book -', len(book_words))
#  Subtracting the words.txt set from the set of dict keys yields
#  words not in words.txt.  set(book_words) deals only with keys
print(len(set(book_words) - eng_set), 'Book words not in dictionary')
for top_wrd, top_cnt in book_words.most_common(20):
    print('{0:.<10s}{1:,d}'.format(top_wrd, top_cnt))
