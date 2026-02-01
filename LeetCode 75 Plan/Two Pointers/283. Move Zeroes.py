class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        right = 0
        length = len(nums)

        while right < length:
            if nums[right]!=0:
                # If we find a non-zero then swap it with left position.
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            right+=1
        return nums


obj = Solution()
print(obj.moveZeroes(nums = [1,0,0,3,12]))