data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@') #find starting char
print(atpos)
sppos = data.find(' ',atpos) #find white space after starting char
print(sppos)
host = data[atpos + 1:sppos] #get string after starting char and before white space
print(host)
