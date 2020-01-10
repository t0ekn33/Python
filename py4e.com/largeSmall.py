largest = None
print("Before:", largest)
for itervar in [3, 41,12,9,74,15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop:", itervar, "Largest:", largest)
print("Largest:", largest)


smallest = None
print("Before:", smallest)
for svar in [3, 41, 12, 9, 75, 1]:
    if smallest is None or svar < smallest:
        smallest = svar
    print("Loop:", svar, "Smallest:", smallest)
print("Smallest:", smallest)

def min(values):
    smaller = None
    for value in values:
        if smaller is None or value < smaller:
            smaller = value
        return smaller
