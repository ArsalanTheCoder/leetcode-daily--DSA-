class Solution(object):
# First Approach
    # def moveZeroes(self, nums):
    #     left = 0
    #     for right in range(len(nums)):
    #         if nums[right]!=0:
    #             if nums[right]!=nums[left]:
    #                 nums[left],nums[right] = nums[right], nums[left]
    #             else:
    #                 left+=1
    #     print(nums)

# Second Approach more faster 
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left] = nums[right]
                left+=1

        for i in range(left, len(nums)):
            nums[i] = 0

        print(nums)    
                            


obj = Solution()
obj.moveZeroes(
 [1,0,1]
)
