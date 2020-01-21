""" Ex3a
Create a program that reads a temperature in degrees Fahrenheit
from the keyboard, then prints the equivalent Centigrade temp.
Remember:
Fahrenheit = 9/5*Centigrade + 32
Centigrade = 5/9*(Fahrenheit –32)
"""

temp = input('Enter temp: ')
# print(temp, type(temp))   # string
fahrenheit = float(temp) # convert to float
centigrade = 5 / 9 * (fahrenheit - 32)

print('{0:.1f}'.format(fahrenheit), 'degrees Fahrenheit is', '{0:.1f}'.format(centigrade), 'degrees in Centigrade')

# Using f-strings
print(f'{fahrenheit:.1f} degrees Fahrenheit is {centigrade:.1f} degrees Centigrade')  
