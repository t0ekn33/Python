"""lab06_timestable.py

Using a while loop within a while loop, produce a 9x9 table showing
all of the results possible for multiplying two single-digit numbers
together.
"""

num1 = 1
while num1 < 10:
    num2 = 1
    while num2 < 10:
#        print('{0:2d}'.format(num1 * num2), end=' ')
        print(f'{num1 * num2:2d}', end=' ')  # format with f-string
        num2 += 1
    print()  # A print statement without arguments just produces a new line.
    num1 += 1
