"""Lab 06
Using range(-40, 120, 10) as input, create three comprehensions.
Assume the values in the range represent Fahrenheit temperatures.
The comprehensions should calculate the corresponding Centigrade
temperature. (Centigrade = 5.0/9.0 * (Fahrenheit - 32))
• Create a list and a set using comprehensions. Both the list and the
set should contain tuples which contain each
Fahrenheit/Centigrade pair. Exclude the entries for Fahrenheit
temperatures zero and 50.
• Create a dictionary comprehension with the Fahrenheit
temperatures as keys and Centigrade temperatures as values. Use
the same exclusions as above.
"""

# convert fahrenheit to celcius

newtmp1 = [5/9*(tmp1-32) for tmp1 in range(-40,120,10)]
for item in newtmp1:
    print(newtmp1)

# y = {(x, x**2) for x in range(5)}
newtmp2 = {(tmp2, 5/9*(tmp2-32)) for tmp2 in range(-40,120,10)}
print(newtmp2)

# z = {x: chr(x+65) for x in range(20)}
newtmp3 = {tmp: 5/9*(tmp-32) for tmp in range(-40,120,10)}
print(newtmp3.items)