"""LAB 06c
In your data file is a program named servercheck.py. It reads two files
(servers and updates) and converts the contents into two sets. The
updates are not always correct. You will find all of the set
operations/methods in Python Notes. Using just these
operations/methods, your job is as follows:
1. Determine whether the list of updates exists in the master server list.
Print a message indicating whether or not this is true.
2. If it is not true (and you know it isn't), create a new set containing the
update items that are NOT in the master server set. Print the number
and names of the unmatched servers.
3. Create a new master server set that excludes the valid updates.
4. Print the number of items in the original master server set and the
new master server set as well as the number of valid updates.
5. Write the contents of the new master server set to a printable
external file using the writelines file method. (See Python Notes)
"""

#reads two files (servers and updates) and converts the contents into two sets
updates = set(open('Python2/Labs/serverupdates.txt', 'r'))
servers = set(open('Python2/Labs/servers.txt', 'r'))
#print(updates)
#print(servers)

# Determine whether the list of updates exists in the master server list.
both = servers.intersection(updates)
#print(both)
#Print a message indicating whether or not this is true.

found = updates.issubset(servers)
if found == True:
    print("Some updates not found in master list.")

"""
If it is not true (and you know it isn't), create a new set containing the
update items that are NOT in the master server set. Print the number
and names of the unmatched servers.
"""
diff = updates.difference(servers)
cnt=0
for i in diff:
    cnt+=1
print(cnt, "server updates not found.")
for i in diff:
    print(i, end=" ")

inter = updates.intersection(servers)
icnt = 0
for i in inter:
    icnt+=1
print("Valid Updates:",icnt)

scnt = 0
for i in servers:
    scnt+=1
print("Original Servers:",scnt)

uniq = updates.union(servers)
ucnt = 0
for i in uniq:
    ucnt+=1
print("New Servers:",ucnt)

# Print the number of items in the original master server set and the
# new master server set as well as the number of valid updates

#writelines
#uniq.writelines()

#print(uniq.issubset(diff)) #False
#print(uniq.issuperset(diff)) #True