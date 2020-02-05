def sumtree(lst):
    tot = 0
    for x in lst:
        if isinstance(x, list):
            tot += sumtree(x)
            print('b', tot)
        else:
            tot += x
            print('a', tot)
    return tot

multi_lst = [1, [2, [3, 4], 5],6, [7, 8]]
print(sumtree(multi_lst))