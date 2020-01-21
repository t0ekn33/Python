""" Lab14
Create a plan and write a program to read the file in your data folder
labeled trees.dat. This file contains the measurement in even feet of the
height of a sampling of California coastal redwood trees. Your job is to
read the data and produce a report showing the following information:
The number of trees in the sample,
The average height of all the trees to the nearest tenth of a foot,
The height of the tallest tree,
The height of the shortest tree, and
The number of trees over 300 feet tall
Format the data so the report has a professional look. Watch for bad
data.
"""
# calculate average
def avgHeight(ttl,cnt):
    avg = ttl / cnt  
    return avg

cnt = 0
ttl = 0
high = 0
low = 1000
over300 = 0

fin = open('trees.dat', 'rt') # Open file
for linein in fin:
    tree = int(linein)
    ttl = ttl + tree # add all lines
    cnt += 1 # count number of lines in file
    
    if(tree > high): # get highest 
       high = tree
    if(tree < low): # get lowest 
        low = tree
    if(tree > 300): # get total
        over300 += 1


avg = avgHeight(ttl,cnt)

print('{0:21s}{1:7d}'.format('Total Trees: ', cnt))
print('Avg height: ', avg) #fix this
print("Tallest Tree: ", high)
print("Shortest Tree: ", low)
print("Over 300 Feet: ", over300)

fin.close() # Close temps.dat file

        
