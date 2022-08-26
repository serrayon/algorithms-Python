

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

#this similar to previous but it returns the index of the numbers used.
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


#This brings back index using the the second print statement
def twoSum(nums, target):
    nums.sort()
    hashTable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashTable:
            print('The combination of:',complement,'and',nums[i],'add up to,',target)
            print([hashTable[target - nums[i]],i],nums)
        else:
            hashTable[nums[i]]= i
input_list = [2,8,12,15,5,17,3]

twoSum(input_list, 20)


#This brings back the index using index method

def sumPairs(arr,pairsSum):
    arr.sort()
    hastable = { }
    for i in range(len(arr)):
        
        complement = pairsSum - arr[i]
        if complement in hastable:
            index = arr.index(complement) 
            index2 = arr.index(arr[i])
            print('The combo of :', arr[i], 'and',complement,'add up to :',pairSum,'; the index of the integers is :', index,',',index2)
            print(arr)
        hastable[arr[i]] = arr[i]
        
num_arr = [4,5,1,6,8,0,-1,34,-25,1009,3,-25,10]
pairSum = 9

sumPairs(num_arr,pairSum)       
