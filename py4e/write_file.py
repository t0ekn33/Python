file = open('output.txt', 'w')
line1 = "This is line 1\n"

file.write("Line0 text\n")
file.write(line1)
file.close()

file = open('output.txt', 'r')
for line in file:
    print(line)
