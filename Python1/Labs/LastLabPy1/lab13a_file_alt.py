"""lab13a_file_alt.py

This program reads temperatures in fahrenheit from
a file, converts them to centigrade (in a function) and prints the results.
It stops when the input is an empty string (end of file).

Note to Windows folks - I have left the open statements for Windows
in place as comments.  Note the forward slashes.  Python will take care
of this for you.  Do not use back slashes.  If you do, you have to
escape each one (e.g., 'c:\\pydata\\trees.dat') or use raw formatting
which we haven't covered yet.
"""


def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0 / 9.0 * (xtmp-32)
    return nutmp


# filein = open('/home/student/pydata/temps.dat', 'rt')
filein = open('c:/pydata/temps.dat', 'rt')  # Windows file
while True:
    temp = filein.readline()
    if temp == '':
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - %r' % temp)
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
