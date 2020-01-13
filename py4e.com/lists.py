s = 'spam is good'
t = list(s) #create a list from a string
print(t)
words = s.split() #splits on words

print(t[2])
print(words[2])


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])
