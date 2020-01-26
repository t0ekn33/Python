"""lab10_for.py

This program gets a temperature in fahrenheit from
a range function, converts it to centigrade and prints the results.
It loops until it reaches 110 degrees skipping the conversions for
zero and 50 using a continue statement to halt that iteration of
the loop.
"""

for ftemp in range(-40, 120, 10):
    if ftemp == 0 or ftemp == 50:
        continue
    ctemp = 5.0 / 9.0 * (ftemp - 32)
    print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
        ftemp, ctemp))
    if ftemp > 95:
        print("It's very hot!")
    elif ftemp > 80 and ftemp <= 95:
        print("It's hot.")
    elif ftemp > 60 and ftemp <= 80:
        print("It's nice out.")
    elif ftemp > 40 and ftemp <= 60:
        print("It's chilly,")
    else:
        print("It's cold!")

print('Conversions completed')
