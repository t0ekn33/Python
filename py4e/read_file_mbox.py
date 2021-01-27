fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print("file not found", fname)
    exit()
#inp = fhand.read() #read entire file into var inp
#print(len(inp)) # print the length
#print(inp[:20]) #print line 20
count = 0
for line in fhand:
    line = line.rstrip() #remove newline char
    if line.find('@uct.ac.za') == -1: #looks for occurance of the string
        continue
    #if not line.startswith('From:'):
    #    continue
    
    #if line.startswith('From:'):
    #    print(line)
    count += 1
    #print('Line Count:', count)
    print('count:', count, 'subject:', fname)
