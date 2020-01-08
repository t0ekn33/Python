# This program demonstrates assignment statements, comments,
# variable names, the print function, math operator and how
# to continue a long statement

gas_in_tank = 4.5   # We have 4.5 gallons in the tank
miles_to_destination = 400
my_money = 12.37
your_money = 14.63
our_money = my_money + your_money
gas_price = 2.50   # Gas costs $2.50 per gallon
gallons_bought = our_money / gas_price
miles_per_gallon = 27.5
distance_we_can_drive = (gallons_bought + gas_in_tank) * miles_per_gallon

print(miles_to_destination, 'miles to drive')
print('We can cover', distance_we_can_drive,   # Continue a long statement
     'miles with the gas we have')
# print('Can we make it?')
