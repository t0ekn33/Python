"""lab13a_file.py

This program reads temperatures in fahrenheit from a file using a for loop,
converts them to centigrade (in a function) and prints the results.
It doesn't have to test for an end-of-file condition.  The for statement
takes care of all of that and simply ends the loop when the file is
exhausted.
"""


def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 / 9.0 * (xtmp-32)
    return nutmp


# filein = open('/home/student/pydata/temps.dat', 'rt')
filein = open('c:/pydata/temps.dat', 'rt')  # Windows file
for temp in filein:
    try:
        ftemp = float(temp)
    except ValueError:  # Note the new method of formatting below
        print('Input contains non-numeric data - {0!r}'.format(temp))
        continue
    ctemp = fahrenheit_to_centigrade(ftemp)
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

filein.close()
