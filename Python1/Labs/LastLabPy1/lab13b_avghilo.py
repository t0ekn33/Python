"""lab13_file.py

This program reads temperatures in fahrenheit from a file using a for loop,
converts them to centigrade (in a function) and prints the results.
It doesn't have to test for an end-of-file condition.  The for statement
takes care of all of that and simply ends the loop when the file is
exhausted.
"""


def fahrenheit_to_centigrade(xtmp):
    nutmp = 5.0/9.0 * (xtmp-32)
    return nutmp


temp_cnt = 0
temp_sum = 0
temp_hi = -1000
temp_lo = 1000
# filein = open('/home/student/pydata/temps.dat', 'rt')
filein = open('c:/pydata/temps.dat', 'rt')  # Windows file
for temp in filein:
    try:
        ftemp = float(temp)
    except ValueError:  # Note the new method of formatting below
        print('Input contains non-numeric data - {0!r}'.format(temp))
        continue
    ctemp = fahrenheit_to_centigrade(ftemp)
    temp_cnt += 1
    temp_sum += ctemp
    if ctemp > temp_hi:
        temp_hi = ctemp
    if ctemp < temp_lo:
        temp_lo = ctemp

print('Average Temperature {0:.1f}'.format(temp_sum / temp_cnt))
print('High Temperature {0:.1f}'.format(temp_hi))
print('Low Temperature {0:.1f}'.format(temp_lo))
filein.close()
