"""Lab 03a
Go back to the last lab and create the dictionary from words.txt by
using the fromkeys method. Remember, you have to remove the
newline character from each word. Consider reading the whole file
into memory and using the splitlines method.
My version of the last lab is available online.
"""

from string import punctuation

"""Process the files"""
words = {} # Dictionary for all the words in words.txt
with open('Python3/Labs/words.txt', 'r') as fin:
    # Read the whole file using splitlines then create a dict
    wordsfin = fin.read().splitlines()
    words = dict.fromkeys(wordsfin, 0)
        # words[word] = 0  # initialize all dictionary counters to zero
    print('Words in dictionary - {0:,d}'.format(len(words)))
unfound_words = set()  # Set to keep words not located in dictionary.
with open('Python3/Labs/alice_in_wonderland.dat', 'r') as fin:
    bookin = fin.read().lower()  # read in the entire book and lower the case

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