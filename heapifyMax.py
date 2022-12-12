def heapify(arr,n,i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[i] < arr[l]:
        largest = l 
    if r < n and arr[largest] < arr[r]:
        largest = r 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
tst=[76,54,34,34,65,78,890,789,45,2323,34,45,45,5423,542,4,543,54325,476,6547,65465,24]
heapSort(tst)
n = len(tst)
print(f'The order list is ')
for i in range(n):
    print(tst[i],end=' ')
