""" Lab08a
Re-implement a previous lab to use a function to do just the
temperature conversion formula.
Call the function from the main program, and return the
centigrade temperature from the function.

Create a new program from the previous lab to print out a
description along with the centigrade temperature.
For Fahrenheit temperatures in the following ranges,
print the corresponding description along with the centigrade
conversion:
Temperature:
Over 95 It’s very hot!
Over 80 to 95 It’s hot
Over 60 to 80 It’s nice out
Over 40 to 60 It’s chilly
40 or less It’s cold!
"""

def fahr2cent(temp):
    # print(temp, type(temp))   # string
    fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (fahrenheit - 32)
    return centigrade

answer = input('Press Enter to begin')
while answer != 'q' and answer != 'Q':
    temp = input("Enter a temperature: ")
    fahrenheit = int(temp)
    centigrade = fahr2cent(temp)

    # print('{0:.1f}'.format(fahrenheit), 'degrees Fahrenheit is', '{0:.1f}'.format(centigrade), 'degrees in Centigrade')

    # Using f-strings
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
    answer = input('Press Enter to continue or q/Q to Quit: ')
        
