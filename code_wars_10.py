def delete_nth(order,max_e):
    for i in range(len(order) - 1, 0, - 1):
        if order.count(order[i]) > max_e:
            order.pop(i)
    return order
    