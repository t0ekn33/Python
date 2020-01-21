""" Lab13b
Change the last lab to remove the descriptions
(in the if/elif/else statements).  Instead, read the same data
accumulating the information necessary to print the following
centigrade temperatures:
•the average centigrade temperature
•the highest centigrade temperature
•the lowest centigrade temperature
Print these results in a neat readable form.
"""

def fahr2cent(temp):
    fahrenheit = float(temp) # convert to float
    centigrade = 5 / 9 * (fahrenheit - 32)
    return centigrade

cnt = 0
temp_total = 0
high = -1000
low = 1000

fin = open('temps.dat', 'rt') # Open temps.dat file
for linein in fin:
    try:
        fahrenheit = int(linein) # convert to intiger
    except ValueError:
        print("Input contains non-numeric data -", '{0!r}'.format(linein))
        continue
    centigrade = fahr2cent(linein) #convert to celcius
    temp_total = temp_total + centigrade # total temp value
    cnt += 1 # count number of lines in file
    if(centigrade > high): # get highest num
        high = centigrade
    if(centigrade < low): # get lowest num
        low = centigrade

avg = temp_total / cnt  # calculate average

print("Avg temp: ", f'{avg:.1f}')
print("High temp: ", high)
print("Low temp: ", f'{low:.1f}')

fin.close() # Close temps.dat file

        
