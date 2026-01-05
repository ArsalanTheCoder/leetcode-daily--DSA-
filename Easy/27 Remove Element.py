class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)-1

        while left<=right:
            if nums[left]==val:
                nums[left]=nums[right]
                right-=1
            else:
                left+=1
      
        return left


obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))
print(obj.removeElement([3,2,2,3], 3))
#Done
