"""Lab07
Change the program you developed in the last lab to remove the
newline characters from the data you read in. Then you have to put
them back in the data you write. In this case, how will you read the
server data? How will you write the new server file? Be sure to
answer these questions before you write any code. When finished,
you should be able to open the new server file with any text editor
and have it display one server per line.
"""


#updates = set(open('Python2/Labs/serverupdates.txt', 'r'))
openupdates = open('Python2/Labs/serverupdates.txt', 'r')

tempupdates = openupdates.read()
updates = tempupdates.splitlines()
print(updates)
servers = set(open('Python2/Labs/servers.txt', 'r'))
#updates = set(open('/home/student/pydata/serverupdates.txt', 'r'))
#servers = set(open('/home/student/pydata/servers.txt', 'r'))

if updates.issubset(servers):  # one way to test
    print('All updates found in master list')
else:
    print('Some updates not found in the master list')
    
# One way to isolate the unmatched servers
diff = updates.difference(servers) 
if len(diff) > 0:
    print(len(diff), 'server updates not found')
    for server_name in diff:
        print(server_name, end='')


fout = open('Python2/Labs/newmaster.txt', 'w')
newset = servers.difference(updates) # or newset = servers - updates
print('Original servers', len(servers), '\nValid updates',
      len(updates) - len(diff), '\nNew servers', len(newset))
fout.writelines(newset)
fout.close()