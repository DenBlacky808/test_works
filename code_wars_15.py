def order_weight(strng):
    orig_l = strng.split()
    print(orig_l)
    for i in range(len(orig_l)):
        min = i
        for j in range(i + 1, len(orig_l)):
            if sum(map(int, list(orig_l[min]))) > sum(map(int, list(orig_l[j]))):
                min = j
            elif sum(map(int, list(orig_l[min]))) == sum(map(int, list(orig_l[j]))):
                if orig_l[min] > orig_l[j]:
                    min = j
        if min != i:
            orig_l[min], orig_l[i] = orig_l[i], orig_l[min]
    return ' '.join(orig_l)


def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
    