class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        current = 0
        
        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Remember: Do NOT increment current here, 
                # we need to check the new number we just swapped in!
            else:
                current += 1
        print(nums)


obj = Solution()
obj.sortColors( nums = [2,0,2,1,1,0])