

x = int(input('Enter an integer: '))
savex = x
fact = 1
while x > 0:
    fact *= x
    x -= 1
print('{0:,d} factorial is {1:,d}'.format(savex, fact))
