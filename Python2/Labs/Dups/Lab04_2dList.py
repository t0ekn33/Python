from pprint import pprint

names = ["jim", "tom", "jack", "mary", "tom", "mary", "tom", "jim", "tom", "mary"]

name_count = []
for name in names:
    for entry in name_count:
        if entry[0] == name:
            entry[1] += 1
            break
    else:
        name_count.append([name, 1])

name_count.sort()
pprint(name_count)