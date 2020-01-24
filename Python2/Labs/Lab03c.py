"""LAB 03c
Read the trees.dat file putting each valid element into a list.
The file contains the height in even feet of a large sample of
California coastal redwood trees. When finished, use only builtin functions (min, max, sum, len) and normal math equations to
produce a report on the screen showing:
• the number of trees,
• the average height of the trees to one decimal place,
• the height of the tallest tree, and
• the height of the shortest tree.
"""
trees = []
fin = open("Python2/Labs/trees.dat", "rt")

for tree in fin:
    tree = tree.strip()
    trees.append(int(tree))

#print(trees)
lenTree = len(trees)
maxTree = max(trees)
minTree = min(trees)
sumTree = sum(trees)
avgTree = sumTree / lenTree
print("Total trees:", lenTree)
print("Tallest tree:", maxTree)
print("Shortest tree:", minTree)
print("Total tree:", sumTree)
print("Average height:", avgTree)