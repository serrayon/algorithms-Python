import time

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return myList
def main():
    st = time.time()
    test = [9,8,7,6,7,8,9,6,5,4,3,2,7,6,8,6,]
    print(mergeSort(test))
    et = time.time()
    elapsedTime = et-st
    print(f'The elapsed time is : {elapsedTime} seconds')
if __name__=='__main__':
    main()



#cleaner and easier to follow
def merge(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left = merge(left)  # Recursive call to sort the left sublist
    right = merge(right)  # Recursive call to sort the right sublist

    # Merge the sorted left and right sublists
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])  # Append any remaining elements from left
    result.extend(right[j:])  # Append any remaining elements from right

    return result

bin = [87, 56, 34, 4356, 76, 678, 56, 3423, 3456, 67, 0, -9, 5, 87, 0, .9, -.9]
print(merge(bin))

