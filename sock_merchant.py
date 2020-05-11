def sockMerchant(n, ar):
    # getting all the index count of given array
    index_dict = {}
    for data in ar:
        index_dict[data] = len([index for index, number in enumerate(ar) if number == data])
    pairs_list = []
    for values in index_dict.values():
        if values % 2 == 0:
            pairs_list.append(values)
        else:
            if values !=0:
                pairs_list.append(values-1) 
    pairs = 0  
    for num in pairs_list:
        if num==2:
            pairs += 1 
        else:
            val = num/2
            pairs += val
    return int(pairs)        
        