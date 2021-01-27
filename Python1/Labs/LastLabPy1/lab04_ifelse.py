
"""lab04_ifelse.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade and prints the results.
Then it prints a message as to whether it is hot outside using
an if/else combination.
"""

temp = input('Enter a temperature: ')
ftemp = float(temp)
ctemp = 5.0/9.0 * (ftemp - 32)
print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
    ftemp, ctemp))
if ftemp > 90:
    print("It's hot outside")
else:
    print("It's not hot outside")
