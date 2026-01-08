class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:
            return len(nums)
        
        left = 2 # first two elements are always allowed
        for right in range(2, len(nums)):
            if nums[right] != nums[left-2]:
                nums[left] = nums[right]
                left+=1
        print(nums)

        return left
   
   
   
obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,3,3]))

#Done

# Has this number already appeared twice
# If YES → skip
# If NO → keep it

# ⏱️ Complexity
# Time: O(n)
# Space: O(1)

