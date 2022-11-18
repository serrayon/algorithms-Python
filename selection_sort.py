'''
not stable, this version will incorrectly place -2 in the wrong spot. The second version without the min_value variable works though.
Quick sort, heap sort and selection not stable'''
#bubble,merge, insertion, and count are unstable

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
