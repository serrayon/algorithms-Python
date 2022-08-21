

def sumPairs(arr, pair):
    # search first element in the array
    for i in range(len(arr)-1):
        # search other element in the array
        for j in range(i+1,len(arr)):
            # if these two elements sum to pair, print the pair
            if arr[i] + arr[j] == pair:
                print("The target number",pair,"is: (",arr[i], ",",arr[j],")")
                
bin = [1,3,6,4,9,7]
pairSum = 10
sumPairs(bin,pairSum)

//this similar to previous but it returns the index of the numbres used.
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




def sumPairs(arr,pairsSum):
    arr.sort()
    hastable = { }
    for i in range(len(arr)-1):
        
        complement = pairsSum - arr[i]
        if complement in hastable:
            index = arr.index(complement) 
            index2 = arr.index(arr[i])
            print('The combo of :', arr[i], 'and',complement,'add up to :',pairSum,'; was represented as:', index,index2)
            print(arr)
        hastable[arr[i]] = arr[i]
        
num_arr = [4,5,1,6,8,0,-1,34,-25,1009,3,-25,10]
pairSum = 9

sumPairs(num_arr,pairSum)       
