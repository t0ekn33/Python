"""
In the book, "Alice in Wonderland" find the words caterpillar and
gryphon. Read the entire book into memory. Print the location of
the first occurrence of each word (find method). Also, print the
number of times each word occurs in the book (count method).
If you finish early, determine the location of the last occurrence of
each word. There is a method that will do this for you.
"""
fin = open('Python2/Labs/alice_in_wonderland.dat', 'r')
#book = fin.read()
#book = book.lower()
cntCata = 0
cntGryph = 0 

for line in fin:
    line = line.lower()
    cntCata = cntCata + line.count("caterpillar") #count caterpillar
    cntGryph = cntGryph + line.count("gryphon")
print(cntCata)
print(line.find("caterpillar"))
print(cntGryph)
print(line.find("gryphon"))
print(line.rfind("caterpillar"))
fin.close()