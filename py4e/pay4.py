"""
Calculate pay from user input using a function
Give employee 1.5 times hourly pay above 40 hours
"""


hours = input("Enter hours: ")
try:
    hours = float(hours)
except:
    print("Please enter a number.")

rate = input("Enter pay rate: ")
try:
    rate = float(rate)
except:
    print("Please enter a number.")
otHours = 0.0
otRate = 1.5
def computePay(hours, rate):
    pay = hours * rate
    return(pay)
if(hours > 40):
    otHours = hours - 40
    print(otHours)
    pay = 40 * rate + otHours * (otRate * rate)
else:
    pay = computePay(hours, rate)

print(pay)

