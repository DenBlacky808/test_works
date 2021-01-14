def solution(args):
    sec_ml = []
    first_ml = []
    fin_l = []
    fin_2l = []
    result = []
    long_l = list(range(args[0], args[-1] + 1))
    # create first modified list.
    for i in range(len(long_l)):
        if long_l[i] == args[i]:  # if the elements are equal.
            first_ml.append(args[i])  # add element to first modified list.
        else:
            args.insert(i, ' ')  # if the elements are not equal add new empty element.
            first_ml.append(args[i])  # anyway we have to add element to first modified list.
    first_ml.append(' ')  # add empty element in the end of first modified list as key.
    # create second modified list from the first. Which consist empty lists and target lists.
    for el_1 in first_ml:
        if el_1 != ' ':
            sec_ml.append(el_1)
        else:
            fin_l.append(sec_ml)
            sec_ml = []
    # filtering empty lists from second modified list.
    while [] in fin_l:
        fin_l.remove([])
    # cut redundant data and create new traget lists. 
    for el in fin_l:
        if len(el) > 2:
            fin_2l.append([el[0], el[-1]])
        else:
            fin_2l.extend(el)
    # last steps in formatting
    for el in fin_2l:
        if isinstance(el, list):
            result.append('-'.join(str(x) for x in el))
        else:
            result.append(el)
    return ','.join(str(x) for x in result)
    
    
    def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
    
    
    
    def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b+1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)
