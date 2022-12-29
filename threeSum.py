def threeSum(nums):       
        # special case
        if len(nums) <= 2:
            return []

        result = set()  # result will contain the unique tuples

        nums = sorted(nums) # nlog(n) complexity

        for x in range(len(nums)-2):
            b = x+1          # begining pointer points to next
            e = len(nums)-1  # end pointer points to last element in nums

            while b < e: # while pointers don't cross one another
                val = nums[x]+ nums[b] + nums[e]
                if val == 0: # we have found the sum
                    result.add(tuple(sorted((nums[x],nums[b],nums[e])))) # need to convert to tuple as it's immutable

                    b += 1
                    e -= 1

                if val < 0: # we need to increase the result, so move towards the right side
                    b += 1
                if val > 0:  # we need to decrease the result, so move towards the left side
                    e -= 1
        return result
        
print(threeSum([-1,1,4,-4,9,0,6,4,3,5,-8]))


#version two 
class Solution:
   def threeSum(self, nums):
      nums.sort()
      result = []
      for i in range(len(nums)-2):
         if i> 0 and nums[i] == nums[i-1]:
            continue
         l = i+1
         r = len(nums)-1
         while(l<r):
            sum = nums[i] + nums[l] + nums[r]
            if sum<0:
               l+=1
            elif sum >0:
               r-=1
            else:
                #The next two lines while are used to skip over any duplicate values of nums[l] and nums[r] respectively.
                #These lines use a while loop to increment l (or decrement r) as long as the condition nums[l] == nums[l + 1] (or nums[r] == nums[r - 1]) is true.
                #This helps to ensure that the triplets added to the result list are unique.
               result.append([nums[i],nums[l],nums[r]])
               while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
               while r>0 and nums[r] == nums[r - 1]: r -= 1
               #Finally, the last two lines l+=1 and r-=1 are used to move the indices l and r to the next elements in the nums list.
               #These lines are used to continue the search for more triplets that sum to zero.
               l+=1
               r-=1
      return result
ob1 = Solution()
print(ob1.threeSum([-1,0,1,2,-1,-4]))
