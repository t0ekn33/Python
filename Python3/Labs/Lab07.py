"""Lab 07 - Lambda Functions
Take the program tempconversion.py in your data folder containing
a function and replace the function that does the conversion with a
lambda function to do the same thing. This does require assigning
the lambda function to a variable.
"""

# def fahrenheit_to_centigrade(xtmp):
#     nutmp = 5.0 / 9.0 * (xtmp - 32)
#     return nutmp  # or combine the two in a return statement as below:
#                   # return 5./9.*(xtmp-32)

# Same as above def using a lambda
fahrenheit_to_centigrade = lambda xtmp : 5.0 / 9.0 * (xtmp - 32)

while True:
    temp = input('Enter a temperature: ')
    if temp == 'q' or temp == 'Q':  
        break
    try:
        ftemp = float(temp)
    except ValueError:
        print('Input contains non-numeric data - try again')
        continue
    ctemp = fahrenheit_to_centigrade(ftemp)
    print('{:.1f} degrees Fahrenheit is {:.1f} degrees Centigrade'.format(
        ftemp, ctemp))
