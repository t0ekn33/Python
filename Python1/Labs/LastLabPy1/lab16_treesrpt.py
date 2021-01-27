"""lab16_treesrpt.py

This program reads a file consisting of tree heights.
It checks the data for validity and the counts the number of trees,
totals the height, determines both the tallest and the shortest trees
and counts the number of trees over 300 feet.  When done reading the
data, it calculates the average height of a tree in float format and
prints all the results formatted neatly.  Then, it creates a report
file with the same information.

Note to Windows folks - I have left the open statements for Windows
in place as comments.  Note the forward slashes.  Python will take care
of this for you.  Do not use back slashes unless you escape each one.
"""

cnt = 0
total = 0
tallest = 0
shortest = 1000
over300 = 0
filein = open('c:/pydata/trees.dat', 'rt')
# filein = open('/home/student/pydata/trees.dat', 'rt')
while True:
    linein = filein.readline()
    if linein == '':  # check for end of file.
        break         # exit the loop.
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
avg = float(total) / cnt  # Left over from Python V2
print('\n')  # separate the report from the bad data by two blank lines.
print('        TREE REPORT\n')
print('{0:21s}{1:7d}'.format('Total Trees', cnt))
print('{0:21s}{1:7.1f}'.format('Average Height', avg))
print('{0:21s}{1:7d}'.format('Tallest Tree', tallest))
print('{0:21s}{1:7d}'.format('Shortest Tree', shortest))
print('{0:21s}{1:7d}'.format('Over 300 feet', over300))

"""
For all subsequent writes, notice we are basically using the same material
from above.  We just added \n's to force line feeds.  Above, the print
command does this for us automatically.
"""

fileout = open('c:/pydata/treerpt.txt', 'wt')
# fileout = open('/home/student/pydata/treerpt', 'wt')
fileout.write('        TREE REPORT\n\n')
fileout.write('{0:21s}{1:7d}\n'.format('Total Trees', cnt))
fileout.write('{0:21s}{1:7.1f}\n'.format('Average Height', avg))
fileout.write('{0:21s}{1:7d}\n'.format('Tallest Tree', tallest))
fileout.write('{0:21s}{1:7d}\n'.format('Shortest Tree', shortest))
fileout.write('{0:21s}{1:7d}\n'.format('Over 300 feet', over300))
fileout.close()
