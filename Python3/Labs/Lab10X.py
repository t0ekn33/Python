"""Lab 10
Write a program to calculate a factorial
recursively. In mathematics, the factorial of
a positive integer n is denoted by n! and is
the product of all positive integers less than or
equal to n. For example, 4! = 4 * 3 * 2 * 1 and
5! = 5 * 4 * 3 * 2 * 1 and so on
Your program should receive an integer from
the keyboard and use a recursive function to
resolve it. The table to the right provides some
correct answers for checking your results
"""

def factorial(num):
    diff = 0
    num = int(num)
    print("num",num)
    n = num
    for n in range(num, -1, -1):
        print("n",n)
        diff = num * diff
        n += 1
        num -= 1
        return(diff)

# ans = input("Enter number:")
ans = 4
total = factorial(ans)
print(total)
