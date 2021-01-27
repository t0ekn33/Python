"""LAB 05a
There is a program in your data file called temp_convert.py. It has a
function that converts a Fahrenheit temperature to centigrade.
Change this program to accept a variable number of temperatures
per function call and process all of them. Print the collector
argument and its type. Use the isinstance function to verify the type
of each parameter as you iterate through it. Each parameter should
be either int or float. Reject all others. Test with invalid data.
Example function call:
fahrenheit_to_centigrade(72, -10.5, 'a', 111, 55) # function call
Have the function parse/test the arguments and print all results.
"""

"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results. 
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

def fahrenheit_to_centigrade(*args):
    for i in args:
        if isinstance(i, (int, float)):
            nutmp = 5.0 / 9.0 * (i - 32)
        else:
            print(i, "is bad data!")
            continue
    
        print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
        i, nutmp))
    

temp = [212, 32, 95, 300, -20, "a", "b", True, False]
fahrenheit_to_centigrade(*temp)