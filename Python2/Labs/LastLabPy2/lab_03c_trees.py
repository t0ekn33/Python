"""lab_03c_trees.py

This program reads all of the tree heights in the trees.dat file and
computes the number of trees, the average height, the shortest tree and
the tallest tree. Only built-in functions are used in the calculations.
"""

trees = []
#fin = open('/home/student/pydata/trees.dat', 'rt')
fin = open('c:/pydata/trees.dat', 'rt')
for i in fin:
    try:
        height = int(i)
    except ValueError:
        print('Bad data', i)
        continue
    trees.append(height)

fin.close()
tree_count = len(trees)
avg_height = sum(trees)/tree_count
tallest = max(trees)
shortest = min(trees)

print('Total trees -', tree_count)
print('Average height - {0:.1f}'.format(avg_height))
# print 'Average height - %.1f' % avg_height # Older formatting
print('Shortest tree -', shortest)
print('Tallest tree -', tallest)

