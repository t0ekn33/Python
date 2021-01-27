
"""lab06a_while.py

This program uses an endless loop (while True) to read a temperature
in fahrenheit from the keyboard, convert it to centigrade and print
the results. This technique requires an explicit break out of the loop.
"""

while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':  # The variable name must be repeated.
        break
    ftemp = float(temp)
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

print('Conversions ended')
