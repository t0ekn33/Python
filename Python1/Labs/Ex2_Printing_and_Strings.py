""" Printing

The print function has a number of options shown in this program
"""

anum = 3.45
bnum = 6
print('Print variables', anum, bnum)
print('Print an expression', anum + bnum)

print('Print variables', anum, bnum, end = ' ')
print('Print an expression', anum + bnum)

print('Print variables', anum, bnum, sep = '->')
print('Print an expression', anum + bnum, sep = ' *-* ')

print('Print variables\n', anum, bnum)
print('Print an expression\n', anum + bnum)

print('Print variables\n', '\t', anum, '\t', bnum)
print('Print an expression\n', '\t', anum + bnum)

print('I am 5\' 10" tall')
print("I am 5' 10\" tall")
print("""I am 5' 10" tall""")
print("""
I am a python
programmer in
training
""")
