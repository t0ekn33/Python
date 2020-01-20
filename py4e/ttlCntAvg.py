"""
Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, 
print out the total, count, and average of the numbers. If the user enters anything other than a number, detect 
their mistake using try and except and print an error message and skip to the next number.
"""
cnt = 0
ttl = 0
avg = 0
num = 0

while True:
    num = input("Enter number:")
    if num == "done":
        break
    else:
        try:
            num = float(num)
            ttl += num
            cnt += 1
        except:
            print("Invalid input")
            continue
avg = ttl / cnt
print("ttl", ttl, "cnt", cnt, "avg", avg)