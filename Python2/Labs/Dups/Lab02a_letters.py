"""lab_02a_letters1.py

This program evaluates all of the alphabetic characters in the book,
"Alice in Wonderland."  It counts all of the alphabetic characters as
well as the number of e's used.  It then prints the total number of
letters, the total number of e's and the percent of the total that
are e's.
"""

tot_letters = 0
tot_e = 0

# fin = open('/home/student/pydata/alice_in_wonderland.dat', 'r') # Linux
fin = open('Python2/Labs/alice_in_wonderland.dat', 'r')  # Windows file
bookin = fin.read()
for i in bookin:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        tot_letters += 1
        if i == 'e' or i == 'E':
            tot_e += 1

# Newest formatting
print(f'Total letters: {tot_letters:,d}')
print(f'Total e\'s: {tot_e:,d}')
print(f'{tot_e/tot_letters:.1%} of all the letters are e\'s\n')
# Newer formatting
print('Total letters: {0:,d}'.format(tot_letters))
print('Total e\'s: {0:,d}'.format(tot_e))
print('{0:.1%} of all the letters are e\'s\n'.format(
        tot_e/tot_letters))
# Older formatting - the format function is required to get a
# thousands separator
print('Total letters: %s' % (format(tot_letters, ',d')))
print('Total e\'s: %s' % (format(tot_e, ',d')))
print('%.1f%% of all the letters are e\'s' %  (
        100*tot_e/tot_letters))
fin.close()