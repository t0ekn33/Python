"""Lab 04b
Your data contains a partial program called payday.py. It contains a
pay rate variable valued at 27 dollars per hour. It also contains a
two-dimensional list. Each sublist contains the day of the week and
the hours worked to the nearest quarter hour. Hours worked
Monday through Friday are paid at the normal rate of 27 dollars.
Saturday hours are paid at time and a half (1.5 * 27) and Sunday
hours are paid at double time (2 * 27).
Add the code necessary to process the data in the list and produce a
report showing the total pay for the week. You should process the
list using both techniques shown in sample gLists4.jpg. While
indexing through the sublist is not necessary here, it will be
important later that you understand how to do it.
Pay for the week is $1525.50
"""

"""payday.py

This program processes the two-dimensional list containing the day
of the week and the hours worked for that day.  It recognizes that
Saturday hours are paid at time and a half and Sunday hours are
paid at double time.  It prints the total of the results.
"""
regHrs = 0.0
satHrs = 0.0 
sunHrs = 0.0

pay_rate = 27
week = [['Sunday', 2],
        ['Monday', 8.5],
        ['Tuesday', 6.75],
        ['Wednesday', 9],
        ['Thursday', 9.25],
        ['Friday', 7.75],
        ['Saturday', 7.5]]

# Unpack sublist method
for i,j in week:
    if i == "Sunday":
        sunHrs = sunHrs + j
        sunPay = sunHrs * (2 * pay_rate)
        #print("su", sunHrs, "sup", sunPay)
    elif i == "Saturday": 
        satHrs = satHrs + j
        satPay = satHrs * (1.5 * pay_rate)
        #print("sa", satHrs, "sap", satPay)
    else:
        regHrs = regHrs + j
        regPay = regHrs * pay_rate
        #print("r", regHrs, "rp", regPay)
print(regPay + satPay + sunPay)


# Index elements method
