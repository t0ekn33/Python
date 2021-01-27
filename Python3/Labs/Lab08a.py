"""lab08_generator2.py

This program has a generator function which duplicates the builtin
range function.  It accepts from 1 to 3 arguments and generates the
required integers one at a time.  Note the use of return to end the
generator if there is an error.  In that case, the corresponding while
loop never gets started.

For the sake of brevity, no error checking is done on the individual
numbers supplied; just the quantity of arguments.  It is assumed all
the numbers are positive integers and of the proper magnitude.
"""

def myrange(*args):
    x = len(args)
    incr = 1
    if x == 1:
        start = 0
        end = args[0]        
    elif x == 2:
        start = args[0]
        end = args[1]
    elif x == 3:
        start = args[0]
        end = args[1]
        incr = args[2]
    else:
        print('From 1 to 3 integers required.  Received', x)
        return  # Normally, you would raise an exception here.
    while start < end:
        yield start
        start += incr

for y in myrange(5):
    print(y, end = ' ')
print()
for y in myrange(2, 10):
    print(y, end = ' ')
print()
for y in myrange(1, 25, 3):
    print(y, end = ' ')
print()
for y in myrange(0, 1, 25, 3):
    print(y, end = ' ')
print()