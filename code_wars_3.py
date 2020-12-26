def narcissistic(value):
    if sum([pow(int(el), len(str(value))) for el in list(str(value))]) == value:
        return True
    else:
        return False
        