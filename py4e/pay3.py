"""
Calculate pay from user input
Give employee 1.5 times hourly pay above 40 hours
"""


hours = input("Enter hours: ")
try:
    hours = float(hours)
except:
    print("Please enter a number.")
try:
    rate = float(rate)
except:
    print("Please enter a number.")
rate = input("Enter pay rate: ")
otHours = 0.0
otRate = 1.5
if(hours > 40):
    otHours = hours - 40
    print(otHours)
    pay = 40 * rate + otHours * (otRate * rate)
print(pay)
