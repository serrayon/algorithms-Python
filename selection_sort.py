'''
not stable, this version will incorrectly place -2 in the wrong spot. The second version without the min_value variable works though. Quick sort, heap sort and selection not stable'''
#bubble,merge, insertion, and count are unstable




def selection(list_a):
    indexing_length = range(0, len(list_a)-1)
    for i in indexing_length:
        min_value = i 
        
        for j in range(i + 1,len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
            if j != i:
                list_a[i], list_a[min_value] = list_a[min_value], list_a[i]
    return list_a
bin1 = [9,8,7,6,5,4,3,2,0,-9,0,-9,65,-2,-2,0]
print(selection(bin))

def selection(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
bin = [9,8,7,6,5,4,3,2,0,-9,0,-9,65,-2,-2,0]
print(selection(bin))
