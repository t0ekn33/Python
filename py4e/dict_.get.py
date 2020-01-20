"""
count how many times letter appears
"""

word = "brontosaurus"
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


#Better way using .get
word2 = "brontosaurus"
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1 #key and default value, if key exists returns value, otherwise return defaul value
print(d)