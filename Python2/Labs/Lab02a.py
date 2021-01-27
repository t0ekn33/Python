"""
LAB 02a
In your data folder, you will find a file containing the text for the
book, "Alice in Wonderland." Read the entire file into memory.
Using only the tools we have covered so far, scan this text counting
all of the letters regardless of case. Keep a separate count for all
occurrences of the letter 'e' again regardless of case. At the end,
print the total of all letters, the number of e's and the percent of the
total that the e's comprise.
"""

fhand = open('Python2/Labs/alice_in_wonderland.dat', 'r')
# count number of lines
cnt = 0
cnte = 0
book = fhand.read()


for line in book:
    #line = line.upper()
    if line >= "A" and line <= "Z" or line >= "a" and line <= "z":
        cnt += 1
        if line == "e" or line == "E":
            cnte += 1

perc = cnte / cnt * 100
cnt = '{0:,}'.format(cnt) #format using commas
cnte = '{0:,}'.format(cnte)

print("Total Letters:", cnt)
print("Total e's:", cnte)
print(f"{perc:.1f}% of all the letters are e's") #round to .2