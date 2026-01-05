class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left+1


obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # 5
print(obj.removeDuplicates([1,1,2,3,4,5,5]))               # 2
#Done