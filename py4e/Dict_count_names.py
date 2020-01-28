"""
Use get() and provide default value of zero when the key is not in the dict() and add one
"""
counts = dict()
data = "john bill steve john tom joe bill john joe bill john joe tony tom bill john"
names = data.split()

for name in names:
    counts[name] = counts.get(name, 0) + 1 #if name not in counts, default 0 and add 1
print(counts)