"""
Lab 06a
Using the technique described on the previous slide,
create a times table. It should be a matrix of the results of
all possible single-digit multiplications.
Don’t worry about getting numbers aligned unless you finish early.
If this assignment confuses you, just do one loop and print
the value of one variable as it increases.  Then, add another
loop within the one that is working.  Remember, always have a
working program.
"""


x = 1
while x < 6:
    y = 1
    while y < 6:
        print(f'{x * y:2d}', end = ' ')
        y += 1
    print()
    x += 1


print("##############################")

num1 = 1
while num1 < 11:
    num2 = 1
    while num2 < 11:
        print(f'{num1 * num2:2d}', end=' ')  # format with f-string
        num2 += 1
    print()  # A print statement without arguments prints a new line.
    num1 += 1
