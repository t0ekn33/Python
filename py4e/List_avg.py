numlist = list()
while True:
    inp = input("Enter number:")
    if inp == "done": break
    total = float(inp)
    numlist.append(total)

average = sum(numlist) / len(numlist)
print("Avg:", average)
input("Press Enter")

#Old method
total = 0
count = 0
while True:
    inp = input("Enter number:")
    if inp == "done": break
    value = float(inp)
    total = total + value
    count += 1

average = total / count
print("Average:", average)