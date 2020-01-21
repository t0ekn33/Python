""" Lab10
Re-implement the previous lab using a for statement with a range
function to convert to Centigrade the Fahrenheit temperatures from
-40 to 110 in increments of ten degrees
(i.e., -40, -30, -20, ..., 110).
Skip the Fahrenheit temperatures zero and 50 when doing the
conversions.  Use a continue statement to make this happen.
"""

# convert fahrenheit to celcius
def fahr2cent(temp): 
    centigrade = 5 / 9 * (temp - 32)
    return centigrade

for t in range(-40,115,10):
    temp = fahr2cent(t)
    
    if(t == 0 or t == 50):
        continue #short circuit the loop (start over)
    print("F: ", t, " - ", "C: ", temp)


