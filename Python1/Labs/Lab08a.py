""" Lab08a
Re-implement a previous lab to use a function to do just the
temperature conversion formula.
Call the function from the main program, and return the
centigrade temperature from the function.
"""

def fahr2cent(temp):
    # print(temp, type(temp))   # string
    fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (fahrenheit - 32)
    return centigrade

temp = input('Enter temperature: ')
centigrade = fahr2cent(temp)
print("centigrade: ", centigrade)
