"""LAB 05b
Create a copy of the program from Lab 05a and change the main
program to accept a variable number of parameters from the
command line. Send those parameters to your function which is still
accepting a variable number of inputs. As before, have the function
parse/test the arguments using different tools as necessary. Print all
results.
Example command with parameters:
python lab_05.py 72 -10.5 a 111 55 #command line parameters
"""
from sys import argv

def fahrenheit_to_centigrade(*args):
    for i in args:
        try:
            x = float(i)
            #print(type(x))
            nutmp = 5.0 / 9.0 * (x - 32)
            print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(x, nutmp))
        except:
            print(i, "bad data")

fahrenheit_to_centigrade(*argv[1:])