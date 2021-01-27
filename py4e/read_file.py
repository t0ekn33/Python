#fhand = open('py4e.com/HDD.txt', 'r')
fhand = input("Enter file name:")
try:
    fhand = open(fhand)
except:
    print("File not found", fhand)
    quit()
# count number of lines
cnt = 0
for line in fhand:
    line = line.rstrip()
    """
    if line.startswith('The'): #print lines with "The"
        print(line)
    """
    if not "The" in line: #print lines with "The"
        continue
    print(line.upper()) #print uppercase
    cnt += 1
print("Lines:", cnt)

"""
# read each char
inp = fhand.read()
print(len(inp)) #print num of chars
print(inp[:22]) #print first 22 chars
"""