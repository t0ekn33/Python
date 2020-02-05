"""Lab 03b
Go back to the last lab and use the translate and maketrans methods
to deal with the replacement or removal of punctuation. 
"""

from string import punctuation

with open('Python3/Labs/words.txt', 'r') as fin:
#with open('/home/student/pydata/words.txt', 'r') as fin:
    wordsin = fin.read().splitlines()
    words = dict.fromkeys(wordsin, 0) # use the static method fromkeys
print('Words in dictionary - {0:,d}'.format(len(words)))

unfound_words = []  # List to keep words not located in dictionary.
with open('Python3/Labs/alice_in_wonderland.dat', 'r') as fin:
#with open('/home/student/pydata/alice_in_wonderland.dat', 'r') as fin:
    bookin = fin.read().lower()  # read entire book; lower the case

# Replace all punctuation except the ' with spaces.  remove all '
temp = str.maketrans(punctuation, len(punctuation) * ' ',"'" )
bookin = bookin.translate(temp)
# for i in punctuation:
    # print(i)
    # if i == "'":  # Replace all puctuation with spaces except
        # bookin = bookin.replace(i, '') # apostrophes
    # bookin = i.translate(str.maketrans("'", "")) # apostrophes
    # else:
        # bookin = bookin.replace(i, ' ')
        # bookin = i.translate(str.maketrans(i, ' ')) 
wordlist = bookin.split()
print('Words in book - {0:,d}'.format(len(wordlist)))
for word in wordlist:
    if word in words:
        words[word] += 1  # If found, increment counter, otherwise
    else:
        unfound_words.append(word) # add to list of unfound words

wordlist2 = sorted(zip(words.values(), words.keys()))
max_times, max_word = wordlist2[-1]

# Calculate the percentage of dictionary words used in the book.
unused_words = list(words.values()).count(0) # number of words with a zero count
print('Percentage of dictionary words used in the book is {0:.2%}'.format(
      (len(words) - unused_words) / len(words)))
print('The word "{0}" was the most frequently used at {1:,d} times'.format(
    max_word, max_times))
# Remove duplicates from unfound list and sort the result
unique_unfound = sorted(set(unfound_words))
print('Number of book words not found in the dictionary -', len(unique_unfound))
nuline = 0
# Print each word left justified in 13 character spaces, and
# put five words on a line.
print('\n{0}\n'.format('Unfound Words'.center(60)))
for word in unique_unfound:
    print('{0:13s}'.format(word), end=' ')
    nuline += 1
    if nuline >= 5:
        nuline = 0
        print()

print("\n\nWe're done!")