"""
read the lines of the file, break each line into a list of words, 
then loop though each of the words in the line and count each word using a dictionary.
"""
import string
pname = "py4e/" #prepend folder path
fname = input("Filename:")
fname = pname + fname

print(fname)
try:
    fhand = open(fname)
except:
    print("File not found!", fname)
    exit()

counts = dict() #create empty dictionary
for line in fhand:
    line = line.rstrip()    #remove trailing spaces
    line = line.translate(line.maketrans("", "", string.punctuation))   #Removes punctuation
    line = line.lower()     #lowercase
    words = line.split()    #splits on spaces (delimiter) and creates a list
    print(words) 

    #count the number of words in the list
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)