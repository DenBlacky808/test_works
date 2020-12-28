def move_zeros_1(array):
    not_zero = [i for i in array if type(i) == bool or i != 0 or type(i) == 'Null']
    not_zero.extend([0 for a in array if str(a).replace(".", "", 1).isdigit() and a == 0])
    return not_zero
    
def move_zeros_2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    
def move_zeros_3(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
    