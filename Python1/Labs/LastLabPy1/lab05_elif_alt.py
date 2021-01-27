
"""lab05_elif.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade and prints the results.
Then it prints a description of the conditions outside.  Note,
this is a more disciplined way to do the comparisons.
"""

temp = input('Enter a temperature: ')
ftemp = float(temp)
ctemp = 5.0 / 9.0*(ftemp-32)
print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
    ftemp, ctemp))
if ftemp > 95:
    print("It's very hot!")
elif ftemp > 80 and ftemp <= 95:
    print("It's hot.")
elif ftemp > 60 and ftemp <= 80:
    print("It's nice out.")
elif ftemp > 40 and ftemp <= 60:
    print("It's chilly.")
else:
    print("It's cold!")
