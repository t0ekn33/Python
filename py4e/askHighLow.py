"""
Exercise 2: 
Prompts for a list of numbers and at the end prints out both the max and min of the numbers.
"""
num = 0

# create empty list
lst = []
n = int(input("Enter number of elements:"))
try:
    n = int(n)
    # iterate till the range
    for i in range (0, n):
        ele = int(input("Enter elements:"))
        lst.append(ele) # addin the elements
except:
    print("Invalid input")
print(lst)
print(min(lst))
print(max(lst))
