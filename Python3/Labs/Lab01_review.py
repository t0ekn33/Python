"""lab01_review.py

This program reads all of the words defined in the file words.txt and
creates a dictionary using each word as the key with an initial value of
zero.  It isolates each word by reading the entire file into memory and
using splitlines to remove the newline character.  If you read each
record in words.txt, you must use either the strip or rstrip methods to
remove the newline.  It then reads in the entire book, "Alice in Wonderland,"
replaces all of the punctuation with either a space or a null character
and then splits on whitespace to isolate each word as an entry in a
list.  Then it proceeds to compare each word to the contents of the
dictionary keeping a count of each occurrence of each word that is used.
If a word isn't found, it is appended to a list of unfound words.  At
the end it calculates and prints the percentage of dictionary words that
were used in the book, the word that was used the most along with the
number of occurrences and finally, it removes the duplicates from the
unfound words list and prints the result.

In this program the newer method of formatting is used (use of f-string
commented at the end of the program), the highest-used word is found by
sorting the unloaded/zipped dictionary and the number of unused words
is found by counting the zeros in the unloaded values of the dictionary.
"""

from string import punctuation

"""Process the files"""
words = {} # Dictionary for all the words in words.txt
fin = open('Python3/Labs/words.txt', 'r')
#fin = open('/home/student/Labs/words.txt', 'r')
for word in fin.read().splitlines():
    words[word] = 0  # initialize all dictionary counters to zero
print('Words in dictionary - {0:,d}'.format(len(words)))
fin.close()
unfound_words = set()  # Set to keep words not located in dictionary.
fin = open('Python3/Labs/alice_in_wonderland.dat', 'r')
# fin = open('/home/student/Labs/alice_in_wonderland.dat', 'r')
bookin = fin.read().lower()  # read in the entire book and lower the case
fin.close()

"""Process the book and count the words"""
for entry in punctuation:
    if entry == "'":  # Replace all puctuation with spaces except
        bookin = bookin.replace(entry, '') # apostrophes
    else:
        bookin = bookin.replace(entry, ' ')
wordlist = bookin.split()
for word in wordlist:
    if word in words:
        words[word] += 1  # If found, increment counter, otherwise
    else:
        unfound_words.add(word) # add to set of unfound words
wordlist2 = sorted(zip(words.values(), words.keys()))
max_times, max_word = wordlist2[-1]

"""Calculate/print results"""
print('Words in book - {0:,d}'.format(len(wordlist)))
# Calculate the percentage of dictionary words used in the book.
unused_words = list(words.values()).count(0) # number of words with a zero count
print('Percentage of dictionary words used in the book is {0:.2%}'.format(
     (len(words) - unused_words) / len(words)))
print('The word "{0}" was the most frequently used at {1:,d} times'.format(
    max_word, max_times))

print('Number of book words not found in the dictionary -', len(unfound_words))
nuline = 0
# Print each word left justified in 13 character spaces, and
# put five words on a line.
print('\n', 'Unfound Words'.center(60), '\n')
for word in sorted(unfound_words):
    print('{0:13s}'.format(word), end=' ')
#    print(f'{word:13s}', end=' ') # use f-string for printing (Python 3.6+)
    nuline += 1
    if nuline >= 5:
        nuline = 0
        print()

print("\n\nWe're done!")