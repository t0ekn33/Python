"""Determining the size of an object

This program uses the getsizeof function in the sys module to print
the size (in bytes) of any object.  Then the main program sends a wide
variety of objects to be evaluated by this function.  The results are
interesting.  Alternatively, every object has a builtin method called
__sizeof__().  This method can be used as follows:
x = 12
print(x.__sizeof__())
Try it.
"""

import sys

def show_sizeof(x):
    print(type(x), sys.getsizeof(x))

show_sizeof(None)
show_sizeof(3)
show_sizeof(2**63)
show_sizeof(102947298469128649161972364837164)
show_sizeof(918659326943756134897561304875610348756384756193485761304875613948576297485698417)
show_sizeof(321.12345434567654323456789)
show_sizeof(12<20)
show_sizeof('')  # Size of a null string
show_sizeof(' ')
show_sizeof('a bigger string than the one above.')
show_sizeof('a bigger string than the one above\u20ac')
show_sizeof(['item01', 'item02', 'item03'])
show_sizeof(['item01', 'item02', 'item03', 'item04', 'item05', 'item06'])
show_sizeof(range(100000))
show_sizeof(list(range(100000)))
