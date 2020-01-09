#name = input('Enter file:')
file_in = open('py4e.com\HDD.txt', 'rt')
counts = dict()

for line in file_in:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)