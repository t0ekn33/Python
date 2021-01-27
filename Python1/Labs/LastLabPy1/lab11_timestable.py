"""lab11_timestable.py

Produce a 9x9 table showing all of the results possible for
multiplying two single-digit numbers together.
"""

print('Multiplication Table')
for i in range(1, 10):
    for j in range(1, 10):
        print('{0:2d}'.format(i * j), end=' ')
    print()  # A print statement without arguments just produces a new line.

print('\nMultiplication Table')
for i in range(1, 10):
    for j in range(1, 10):
        print('%2d' % (i * j), end=' ') # Use the older formatting
    print()  # A print statement without arguments just produces a new line.

print('\nMultiplication Table')
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:2d}', end=' ')  # Using f-strings. Requires Python 3.6+
    print()  # A print statement without arguments just produces a new line.
