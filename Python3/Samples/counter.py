"""Demo the Counter class

This program demonstrates some of the capabilities of the Counter class
"""

from collections import Counter
x = 'abracadabra'
ltrs = Counter(x)
print(ltrs)  # This object is not act exactly the same as a dictionary
print('Unloaded:', ltrs.most_common()) # This method unloads the object the
# same as dict.items() would except that the result is ordered by value

# Alternative way to populate an instantiation of Counter
ltrs = Counter() # Create an empty Counter
for letter in x:
    ltrs[letter] += 1 # Note this does not fail if the letter is
                      # not already in the Counter
print('Alternative:', ltrs.most_common())  # print all of the tuples

# Another alternative way to populate an instantiation of Counter
ltrs = Counter() # Empty Counter
ltrs.update(x) # Initial population with update method
print('After Update:', ltrs)  # print all of the tuples
z = 'himalayas'  # Define a new string with letters to add
ltrs.update(z) # Additional data added with update method
print(ltrs.most_common())  # print all of the tuples

print('Minus:', ltrs - Counter(z)) # Subtracts and removes all entries < 1
ltrs.subtract(Counter(z))# Subtracts and keeps all results
print('Subtract:', ltrs)
ltrs += Counter() # Removes all entries < 1
print('Remove:', ltrs)

# To get the n most common, use the most_common method with the
# number (n) of the items you want:  obj.most_common(n)
print('Top 3:', ltrs.most_common(3))

# To get the n least common you have to use this slice on the result
# of the most_common method:  obj.most_common()[-1: -n-1; -1]
print('Bottom 3:', ltrs.most_common()[-1: -3-1: -1])  # as an example
# We could have used -4 in the above example in place of -3-1.
# I have found it helps to keep them separate if you are struggling
# to visualize this process.
print('Bottom 3:', ltrs.most_common()[-1: -4: -1])  # Same result as above
