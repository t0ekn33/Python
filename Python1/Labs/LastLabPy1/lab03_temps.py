
"""lab03_temps.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade and prints the results.
Note - the input from the keyboard is a string.  It must be
converted to a number (a float in this case) before the input can
be used in an arithmetic operation.  Also, the two print functions
are continued to a second line using an enclosure (a parenthesis in
this case) which is one way to do it.
"""

temp = input('Enter a temperature: ')
ftemp = float(temp)
ctemp = 5.0 / 9.0 * (ftemp-32)
print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
    ftemp, ctemp))
# Using f-strings
print(f'{ftemp:.1f} degrees Fahrenheit is {ctemp:.1f} degrees Centigrade')  
