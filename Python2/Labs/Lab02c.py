"""
LAB 02c
Using the chr() and ord() built-in functions, print the ASCII characters
corresponding to the numbers 32 through 126. Then, from the
string module, import the variable printable. If necessary, review
the string module through help('string') in the shell or pydoc[3]
string from command line. Afterwards, iterate through the
"printable" string and print out each entry and its corresponding
ordinal. Be sure to use !r ( or the older %r) formatting on the
characters in printable items so you can see the whitespace
characters. My solution to Lab 02b contains an example of !r.
"""
from string import printable

for num in range(32, 127):
    print(chr(num), end=" ")

x = 32 

while x <= 126:
    asci = chr(x)
    print(asci, end = " ")
    x += 1
    
for num in printable:
    print('{0!r:6} {1:d}'.format(num, ord(num))) #print ascii up to 6 places and print (d)ecimal