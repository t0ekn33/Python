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
"""Create a dictionary for counting using the entries from words.txt as the keys."""
fin_words = open("Python2/Labs/words.txt", "r")
dict_words = {}
for word in fin_words:
    if word not in dict_words:
        dict_words[word] = 1
    # dict_words.append(word)
print("Words in English language dictionary: {0:,}".format(len(dict_words)))

# for key in dict_words:
#     print("key:{}, value:{}".format(key,dict_words[key]))
fin_words.close

"""
Parse the text in alice_in_wonderland.data isolating each word. This requires
removing/replacing all punctuation and using the split method. Make sure the
words in the book are all lower case. (Hint: replace all punctuation with spaces
except the apostrophe. Replace it with a zero-length string.
"""
import string
fin_alice = open("Python2/Labs/alice_in_wonderland.dat", "rt")
count = dict()

for word in fin_alice:
    words = word.rstrip()
    words = words.translate(words.maketrans("", "", string.punctuation))
    words = word.lower()
    words = word.split()
    print(words)
    for word in words:
        count[word] = count.get(word, 0) + 1

fin_alice.close


"""
counts = dict() #create empty dictionary
for line in fhand:
    line = line.rstrip()    #remove trailing spaces
    line = line.translate(line.maketrans("", "", string.punctuation))   #Removes punctuation
    line = line.lower()     #lowercase
    words = line.split()    #splits on spaces (delimiter) and creates a list
    print(words) 
"""