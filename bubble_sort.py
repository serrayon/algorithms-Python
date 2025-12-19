import time

def bubble(list_a ):
    
    indexing_length = len(list_a) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        
        for i in range(0 , indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a
def main():
    st = time.time()   
    print(bubble([4,9,0,1,-1,0,3,6,764576]))
    et = time.time()
    elapsedTime = et - st
    print(f'The elapsed time is: {elapsedTime} seconds')
if __name__=='__main__':
    main()

# this does not have to go through the list every time 
def bubble_optimized(arr):
    n = len(arr)

    while n > 1:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break  # list already sorted

        n -= 1  # last element is now in correct position

    return arr
"""
What changed (and why it matters)

Shrinking the inner loop

After each pass, the largest element is guaranteed to be at the end.

So we reduce the range (n -= 1) instead of rechecking it.

Early exit

If no swaps happen in a full pass, the list is already sorted.

We break instead of looping again.

Complexity (important but honest)

Worst case: O(n²) (same as standard bubble sort)

Best case (already sorted): O(n)

Practical improvement: Fewer comparisons and swaps

Why this is a good learning step

You’re absolutely right:

This helps you understand why list.sort() is faster

You’re learning loop invariants, early termination, and algorithmic optimization

This is exactly “learning to walk before running”
"""
