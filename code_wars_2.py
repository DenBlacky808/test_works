def find_outlier(integers):
    even_list = []
    odd_list = []
    for num in integers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
            odd_list.append(num)
    if len(even_list) > 1:
                return odd_list[0]
    if len(odd_list) > 1:
                return even_list[0]