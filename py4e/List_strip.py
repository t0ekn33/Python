#List strip
fin = open("py4e/mbox-short.txt")
for line in fin:
    line = line.rstrip() #remove trailing whitespace
    if not line.startswith("From"): continue
    words = line.split() #split on whitespace
    print(words[1]) #print emails addys