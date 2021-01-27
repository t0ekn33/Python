
"""lab06a_while.py

This program uses a finite loop (while cond) to read a temperature
in fahrenheit from the keyboard, convert it to centigrade and print
the results. This technique requires a preliminary input to initialize
the variable used in the while condition.  Then, another input at the
end of the loop to get the next temperature to be tested/converted.
"""

temp = input('Enter a temperature: ')
while temp != 'q' and temp != 'Q':   # or
# while not(temp == 'q' or temp == 'Q':
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
    temp = input('Enter a temperature: ')

print('Conversions ended')
