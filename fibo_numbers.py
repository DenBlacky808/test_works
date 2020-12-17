from itertools import count


def fibo_nums(n):
    list_nums = [0]
    a = 0
    b = 1
    for _ in count(0):
        c = a + b
        a = b
        b = c
        if b % 2 == 0:
            list_nums.append(b)
            if len(list_nums) >= int(n):
                break
    return list_nums


print(fibo_nums(input('input ')))
