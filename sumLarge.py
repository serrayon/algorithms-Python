def sumLarge(arr):
    
    total = 0 
    for i in range(0,len(arr)):
        
        total = total + arr[i]
    return total
    
bin = [1,210009,65346354,3654354774635,-10000000000000000]
print(sumLarge(bin))
