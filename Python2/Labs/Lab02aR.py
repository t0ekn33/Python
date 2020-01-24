"""LAB 02a Revisited
In your data folder, you will find a file containing the text for the book,
"Alice in Wonderland. Read the entire file into memory. Using only the
tools we have covered so far, scan this text counting all of the letters.
Keep a separate count for all occurrences of the letter 'e'.
Review the program you produced for this lab and use the string
methods we have covered to simplify the code.
Answers:
Total Letters: 107,720
Total e's: 13,575
12.6% of all the letters are e's
"""


fhand = open('Python2/Labs/alice_in_wonderland.dat', 'r')
cnt = 0
cnte = 0

book = fhand.read() #read into memory
book = book.upper() #convert to upper

for line in book:
    if line.isalpha():
        cnt += 1 #count all letters
        cnte = cnte + line.count("E") #count all E's

perc = cnte / cnt * 100
cnt = '{0:,}'.format(cnt) #format using commas
cnte = '{0:,}'.format(cnte) 

print("Total Letters:", cnt)
print("Total e's:", cnte)
print(f"{perc:.1f}% of all the letters are e's") #round to .2