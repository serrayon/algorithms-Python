def quick(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    greater_list = [ ]
    lesser_list= [ ]
    
    for item in sequence:
        if item > pivot:
            greater_list.append(item)
        else:
            lesser_list.append(item)
            
    return quick(lesser_list) + [pivot] + quick(greater_list)


print(quick([4,457,3,0,-1,3,5423]))