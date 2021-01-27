"""
Exercise 1: Write a function called chop that takes a list and 
modifies it, removing the first and last elements, and 
returns None. Then write a function called middle that takes a 
list and returns a new list

"""
def chop(list1):
    del list1[0]
    del list1[-1]
    return None

def middle(list2):
    nums = ['1', '2', '3', '4']
    return nums

lets = ['a', 'b', 'c', 'd']
chop(lets)
print(lets)
noms = middle(lets)
print(noms)
