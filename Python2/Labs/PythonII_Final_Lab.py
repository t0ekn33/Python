"""Do the following lab.
In the data from Python II find, "alice_in_wonderland.dat." You will also find a file
labeled, "words.txt." The latter file contains over 100,000 English-language
words. Your job is to perform the following:
Create a dictionary for counting using the entries from words.txt as the keys.
Parse the text in alice_in_wonderland.data isolating each word. This requires
removing/replacing all punctuation and using the split method. Make sure the
words in the book are all lower case. (Hint: replace all punctuation with spaces
except the apostrophe. Replace it with a zero-length string.)
Find each word from the book in your dictionary and increase the count for that
word by one.
If a word is not found in the dictionary, place it in a list with other unfound words.
When you have processed the entire book, determine the percentage of words in
the dictionary that were used in the book and which word was used the most.
Remove the duplicates from the list of unfound words, sort it and print it using
the same format shown on the next slide.
Don't try too hard to make this perfect. It won't happen!
The output from your program should look something like the following:
Words in English language dictionary - 113,810
Words in book - 26,694
Percentage of dictionary words used in the book is 2.19%
The word "the" was the most frequently used at 1,644 times
"""
import string
dict_words = dict()
list_unfound = list()
lst = list()
acnt = 0
dcnt = 0

# Read in words.txt and remove "\n"
list_words = open("Python2/Labs/words.txt", "rt").read().split("\n")

# Create a dictionary for counting using the entries from words.txt as the keys.
for word in list_words:
    dict_words[word] = dict_words.get(word,0) + 1

# Open book
fin_alice = open("Python2/Labs/alice_in_wonderland.dat", "rt")

# List of words in book, removed spaces & punctuation, lowercase
for word in fin_alice:
    word = word.rstrip()
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.lower()
    list_alice = word.split()
    for word in list_alice:
        acnt += 1
        if word in dict_words:
            dcnt += 1
            dict_words[word] += 1
        else:
            list_unfound.append(word)
            list_unfound.sort()

# Sort dict_words by value in reverse to get most used
for key, val in list(dict_words.items()):
    lst.append((val, key))
lst.sort(reverse=True)

# Remove dups in list
list_unfound = list(dict.fromkeys(list_unfound))

print("Words in English language dictionary: {0:,}".format(len(dict_words)))
print("Words in book: {0:,}".format(acnt))
# Percentage of words in the dict that were used in the book
perc = (dcnt / len(dict_words) * 10)
print("Percentage of dictionary words used in the book is {0:.2f}%".format(perc))
for key, val in lst[:1]: # Only show most used word, slicing off after 1
    print("The word \"{1}\" was the most frequently used at {0:,} times.".format(key, val))
print()
input("Press <Enter> to see words not in the dictionary...")
print()
print(*list_unfound, sep=", ")

fin_alice.close()