import itertools


def permutations(string):
    new_list = []
    if len(string) == 1:
        new_list.append(''.join(string))
    else:
        for chars in itertools.permutations(list(string), len(string)):
            new_list.append(''.join(chars))
    return list(set(new_list))


import itertools


def permutations(string):
    return list(set([''.join(string) if len(string) == 1 else ''.join(chars) for chars in
                     itertools.permutations(list(string), len(string))]))
