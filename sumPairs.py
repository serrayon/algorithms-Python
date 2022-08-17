

def sumPairs(arr, pair):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == pair:
                print("The target number",pair,"is: (",arr[i], ",",arr[j],")")
                
bin = [1,3,6,4,9,7]
pairSum = 10
print(sumPairs(bin,pairSum))


def sumPairs(arr, pair_sum):
    hashTable = { }
    
    for i in range(len(arr)-1):
        complement = pair_sum - arr[i]
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (",arr[i],",",complement,")")
        hashTable[arr[i]] = arr[i]
        
num_arr = [4,5,1,8,0,-1,34,34,-25,1009,-1000,pow(3,2)]
pairSum = 9
sumPairs(num_arr,pairSum)  
