"""
read the lines of the file, break each line into a list of words, 
then loop though each of th ewords in the line an dcount each word using a dictionary.
"""

fname = input("Filename:")
try:
    fhand = open(fname)
except:
    print("File not found!", fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)