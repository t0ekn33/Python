"""
Lab 11
Using the for-loop technique described on the previous slide,
create a times table.
Use the results of Lab 06b and modify these using for loops.
"""

for x in range(1,10): # iterate 1-9
    for y in range(1,10): # iterate 1-9 * above 1-9
        print(f'{x * y:2d}', end = ' ')
    print() # Print next line

print("######## same as above using while loop ########")

x = 1
while x < 10:
    y = 1
    while y < 10:
        print(f'{x * y:2d}', end = ' ')
        y += 1
    print()
    x += 1


