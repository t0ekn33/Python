""" Lab09
Re-implement a previous lab to use a try statement to catch
ValueError exceptions. Test by entering a non-numeric temperature.
"""

# convert fahrenheit to celcius
def fahr2cent(temp): 
    # print(temp, type(temp))   # string
    #fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (temp - 32)
    return centigrade

# convert celcius to fahrenheit
def cent2fahr(temp): 
    # print(temp, type(temp))   # string
    #centigrade = float(temp) # convert to float
    fahrenheit= 9 / 5 * temp + 32
    return fahrenheit

answer = None
while answer != 'q' and answer != 'Q':
    temp = input('Enter temperature: ')
    try:
        temp = float(temp)
    except ValueError:
        print("Bad data -", temp)
        continue
    temp_type = input('Enter c or f: ')
    
    if(temp_type == 'c'):
        fahrenheit = cent2fahr(temp)
        print("fahrenheit: ", fahrenheit)
        
    else:
        centigrade = fahr2cent(temp)
        print("centigrade: ", centigrade)
    answer = input('Press Enter to continue or q/Q to Quit: ')
print("Goodbye!")
