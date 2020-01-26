"""lab08a_func.py

This program reads a temperature in fahrenheit from
the keyboard, converts it to centigrade (in a function) and prints the
results. Then it requests another input from the keyboard.
"""


def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 / 9.0 * (xtmp-32)
    return nutmp  # or combine the two in a return statement as below:
    # return 5.0 / 9.0 * (xtmp-32)

while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':
        break
    ftemp = float(temp)
    ctemp = fahrenheit_to_centigrade(ftemp)  # call the function and save
                                            # the results in ctemp
    print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
        ftemp, ctemp))
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
