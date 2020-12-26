def get_sum(a, b):
    if b > a:
        i_list = [i for i in range(a, b + 1, 1)]
    elif a == b:
        i_list = [a]
    else:
        i_list = [i for i in range(b, a + 1, 1)]
    return sum(i_list)
    