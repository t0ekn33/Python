numlist = list() #create empty list
while (True):
    inp = input('Enter number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value) #add value to numlist list

average = sum(numlist) / len(numlist)
print(average)


