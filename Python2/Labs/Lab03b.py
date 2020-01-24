"""LAB 03b – Filter, Map Reduce
Use the range function to create a list containing the numbers:
[2, 5, 8, 11, 14, 17]
• Use the techniques you have learned so far to:
• Create and print a new list with only the even numbers from the
original list. (filter)
• Create and print another new list containing the square of the
original numbers. (map)
• Create a result showing the sum of all the original numbers.
(reduce)
• Use normal loops to accomplish each of these tasks
"""
even = []
sqr = []
nums = [2, 5, 8, 11, 14, 17]
ttl = 0

for x in nums:
    ttl += x
    if x % 2 == 0:
        even.append(x)
    sqr.append(x**2)
print("Original List:", nums)
print("Filter:", even)
print("Map:", sqr)
print("Reduce:", ttl)