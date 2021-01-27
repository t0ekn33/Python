name = input("Enter filename:")
fin = open("py4e/" + name)

counts = dict()
for line in fin:
    words = line.split() #split on spaces
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #get word, else add word with default 0 and add 1

bigcount = None
bigword = None
for word,count in counts.items(): #gets both items in dict()
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("The word", bigword, "is listed", bigcount, "times")