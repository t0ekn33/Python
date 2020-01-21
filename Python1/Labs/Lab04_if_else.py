""" Lab04
Create a new program from the previous lab to print out a
description along with the centigrade temperature.
For Fahrenheit temperatures that are above 90 degrees,
print “It’s hot outside”.  Otherwise, print “It’s not hot outside”.  This printing should follow the printing showing the conversion from Fahrenheit to Centigrade.
"""

temp = input('Enter temp: ')
# print(temp, type(temp))   # string
fahrenheit = float(temp) # convert to float
centigrade = 5 / 9 * (fahrenheit - 32)

# print('{0:.1f}'.format(fahrenheit), 'degrees Fahrenheit is', '{0:.1f}'.format(centigrade), 'degrees in Centigrade')

# Using f-strings
print(f'{fahrenheit:.1f} degrees Fahrenheit is {centigrade:.1f} degrees Centigrade')  

if fahrenheit > 90:
    print('It\'s hot outside')
else:
    print('It\'s NOT hot outside')
        
