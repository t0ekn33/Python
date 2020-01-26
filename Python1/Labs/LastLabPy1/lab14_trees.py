"""lab14_trees.py

This program reads a file consisting of tree heights.
It checks the data for validity and then counts the number of trees,
totals the height, determines both the tallest and the shortest trees
and counts the number of trees over 300 feet.  When done reading the
data, it calculates the average height of a tree in float format and
prints all the results formatted neatly.

Note to Windows folks - I have left the open statements for Windows
in place as comments.  Note the forward slashes.  Python will take care
of this for you.  Do not use back slashes.  If you do, you have to
escape each one (e.g., 'c:\\pydata\\trees.dat') or use raw formatting
which we haven't covered yet.
"""

cnt = 0
total = 0
tallest = 0
shortest = 1000
over300 = 0
filein = open('c:/pydata/trees.dat', 'rt')
#  filein = open('/home/student/pydata/trees.dat', 'rt')
for linein in filein:
    try:
        height = int(linein)
    except ValueError:
        print('Bad Data - {0!r}'.format(linein))
        continue    # go back to the beginning of the loop.
    cnt = cnt + 1
    total = total + height
    if height < shortest:
        shortest = height
    if height > tallest:
        tallest = height
    if height > 300:
        over300 = over300 + 1

filein.close()
# avg = float(total) / cnt  # Python V2
avg = total / cnt
print('\n')  # separate the report from the bad data by two blank lines.
print('        TREE REPORT\n')
print('%-21s%7d' % ('Total Trees', cnt))
# The - in the old format forces left justification.
# The default is right justification for all data
print('%-21s%7.1f' % ('Average Height', avg))
print('%-21s%7d' % ('Tallest Tree', tallest))
print('%-21s%7d' % ('Shortest Tree', shortest))
print('%-21s%7d' % ('Over 300 Feet', over300))
print()
# The new format right justifies numerics and left justifies otherwise
# Also, the d format type causes an error if it encounters a float.
# This doesn't happen in the old formatting.
print('{0:21s}{1:7d}'.format('Total Trees', cnt))
print('{0:21s}{1:7.1f}'.format('Average Height', avg))
print('{0:21s}{1:7d}'.format('Tallest Tree', tallest))
print('{0:21s}{1:7d}'.format('Shortest Tree', shortest))
print('{0:21s}{1:7d}'.format('Over 300 feet', over300))
print()
#  And these use f-strings
print(f'{"Total Trees":21s}{cnt:7d}')
print(f'{"Average Height":21s}{avg:7.1f}')
print(f'{"Tallest Tree":21s}{tallest:7d}')
print(f'{"Shortest Tree":21s}{shortest:7d}')
print(f'{"Over 300 feet":21s}{over300:7d}')
