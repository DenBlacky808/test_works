from itertools import count


def find_nb(m):
    em = 0
    for n in count(0):
        em = em + pow(n, 3)
        if em == m:
            return n 
        elif em > m:
            return -1
            