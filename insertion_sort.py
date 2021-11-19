def insertion(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i] 
        
        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i -1] = list_a[i -1],list_a[i]
            i = i - 1
    return list_a
print(insertion([3,6,6534,7,83,54325,0]))