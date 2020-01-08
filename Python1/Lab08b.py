""" Lab08b
Create a program that reads a temperature from the keyboard.
It should then read a second input, a single character,
that determines what type of conversion to perform.  A 'c'
causes a fahrenheit-to-centigrade conversion while 'f' causes
the opposite conversion.  Create separate functions to provide
the conversions as well as print statements showing the result
of the conversion. The functions should be void (return None).
After a conversion, the main program should request a new set of
inputs from the keyboard until a 'q' is entered in place of a
temperature.  Also, remember:
Fahrenheit = 9/5*Centigrade + 32
Centigrade = 5/9*(Fahrenheit –32)
"""

# convert fahrenheit to celcius
def fahr2cent(temp): 
    # print(temp, type(temp))   # string
    fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (fahrenheit - 32)
    return centigrade

# convert celcius to fahrenheit
def cent2fahr(temp): 
    # print(temp, type(temp))   # string
    centigrade = float(temp) # convert to float
    fahrenheit= 9 / 5 * centigrade + 32
    return fahrenheit

answer = None
while answer != 'q' and answer != 'Q':
    temp = input('Enter temperature: ')
    temp_type = input('Enter c or f: ')
    
    if(temp_type == 'c'):
        fahrenheit = cent2fahr(temp)
        print("fahrenheit: ", fahrenheit)
        
    else:
        centigrade = fahr2cent(temp)
        print("centigrade: ", centigrade)
    answer = input('Press Enter to continue or q/Q to Quit: ')
print("Goodbye!")
