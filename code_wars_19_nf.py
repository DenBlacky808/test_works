#not_finished
def solution(args):
    clone_l = args
    order_l = []
    n_ord = []
    new_l = []
#     print(clone_l)
    for i in range(len(args)-1):
        if args[i] + 1 == clone_l[i + 1]:
            order_l.append(args[i])
            if len(order_l) >= 3:
            order_l.append(args[-1])        
            new_l.append(order_l)
        elif len(new_l) > 0 and order_l[-1] == clone_l[i - 1]:
            order_l.append(args[i])
            if len(order_l) >= 3:
                new_l.append(order_l)
                order_l = []
        else:
            n_ord.append(args[i]) 
            new_l.append(n_ord)
            n_ord = []
    
    return new_l
