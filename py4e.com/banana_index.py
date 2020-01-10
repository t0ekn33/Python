"""
Write a while loop that start at the last characeter in the string and works ins way backwards to the first
character in the string, printing each letter on a seperate line.
"""

fruit = "banana"
length = len(fruit)
#last = fruit[length - 1]
last = fruit[-1] # this works better
print(last)

index = len(fruit) - 1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index -= 1