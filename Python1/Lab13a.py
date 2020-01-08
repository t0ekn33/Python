""" Lab13a
Re-implement Lab 08a to replace the data source with a file instead
of input().  The file should be the data in the temps.dat file in
your data folder.  Be sure to account for any bad data that might
be contained in this file.
"""

def fahr2cent(temp):
    fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (fahrenheit - 32)
    return centigrade

fin = open('temps.dat', 'rt') # Open temps.dat file
for linein in fin:
    try:
        fahrenheit = int(linein)
    except ValueError:
        print("Input contains non-numeric data -", '{0!r}'.format(linein))
        continue
    centigrade = fahr2cent(linein)
    print(f'{fahrenheit:.1f} degrees Fahrenheit is {centigrade:.1f} degrees Centigrade')  

    if fahrenheit > 95:
        print('It\'s very hot!')
    elif fahrenheit > 80 and fahrenheit <= 95:
        print('It\'s hot!')
    elif fahrenheit > 60 and fahrenheit <= 80:
        print('It\'s nice out')
    elif fahrenheit > 40 and fahrenheit <= 60:
        print('It\'s chilly')
    else:
        print('It\'s cold!')
fin.close() # Close temps.dat file

        
