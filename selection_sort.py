def selection(arr):
    length = len(arr)
    for i in range(length-1):
        minValue=i 
        for j in range(i+1,length):
            if arr[j] < arr[minValue]:
                minValue = j 
        if minValue != i:
            arr[i],arr[minValue]=arr[minValue],arr[i]
    return arr


test = [9,8,7,6,5,4,3,2,1]
print(selection(test))

def selection(moreNumbers):
    length = len(moreNumbers)
    for i in range(length - 1):
        minValue = i 
        for j in range(i+1,length):
            if moreNumbers[j] < moreNumbers[minValue]:
                minValue = j 
        if minValue != i:
            moreNumbers[i],moreNumbers[minValue]=moreNumbers[minValue],moreNumbers[i]
    return  moreNumbers
    
someList = [9,8,-2,7,6,5,4,3,2,1]
print(selection(someList))

'''
not stable, this version will incorrectly place -2 in the wrong spot. The second version without the min_value variable works though.
Quick sort, heap sort and selection not stable'''
#merge(Merge Sort is already stable if implemented properly because merging happens left to right, preserving order.), and quick(naturaly unstable elements can get swapped across partitions.)

def stable_selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        minIndex = i

        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:  
                minIndex = j  

        # Instead of swapping, we shift elements and insert the minimum element
        if minIndex != i:
            minValue = arr[minIndex]
            
            # Shift elements to the right to maintain stability
            while minIndex > i:
                arr[minIndex] = arr[minIndex - 1]
                minIndex -= 1
            
            arr[i] = minValue  # Insert the minValue at its correct position
    
    return arr

# Example with duplicate values
arr = [(3, 'A'), (1, 'B'), (3, 'C'), (2, 'D')]
print(stable_selection_sort(arr))


import time

st = time.time()
def selection(lst):
    indexLength = range(0, len(lst)-1)
    for i in indexLength:
        
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
             
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def main():
    et = time.time()
    elapsed_time = et-st
    test = [0,0,-8,89,76,56,453,34,23,34,564,67,78,54,4334,-9,0]
    print(selection(test))
    print('Execution time: ', elapsed_time, 'seconds')
if __name__=='__main__':
    main()

#stable without the minValue
def selection(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
def main():
    st = time.time()
    bin = [9,8,7,6,5,4,3,2,0,-9,0,-9,65,-2,-2,0]
    print(selection(bin))
    et = time.time()
    elapsedTime = et - st 
    print(f'The elapsed time is: {elapsedTime} seconds')
if __name__=='__main__':
    main()
