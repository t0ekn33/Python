
"""lab10_recursion.py

This program uses recursion to compute a factorial. It also demonstrates
how a function cannot change an immutable argument.  The function
ends up working with its own copy of the argument.
"""

def factorial(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

x = int(input('Enter an integer: '))
print('{0:,d} factorial is {1:,d}'.format(x, factorial(x)))
