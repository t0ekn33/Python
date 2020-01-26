"""lab09_err.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade (in a function) and prints
the results.  Then it requests another input from the keyboard.
It captures erroneous entries rather than letting the program fail.
Then it tells the operator to try again.
"""


def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 / 9.0 * (xtmp - 32)
    return(nutmp)


while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - try again')
        continue
    ctemp = fahrenheit_to_centigrade(ftemp)
#    print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
#        ftemp, ctemp))
    print(f'{ftemp:.1f} degrees Fahrenheit is {ctemp:.1f} degrees Centigrade')
    if ftemp > 100:
        print("It's very hot!")
    elif ftemp > 80:
        print("It's hot.")
    elif ftemp > 60:
        print("It's nice out.")
    elif ftemp > 40:
        print("It's chilly,")
    else:
        print("It's cold!")
