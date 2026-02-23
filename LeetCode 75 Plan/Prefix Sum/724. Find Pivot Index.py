class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_side = 0

        # enumerate gives us 'i' (the index) AND 'num' (the actual number)
        for i, num in enumerate(nums):
            
            # Use our math formula
            right_side = total_sum - left_side - num
            
            # Check for balance
            if left_side == right_side:
                return i
            
            # Add the current number to the left side for the next step
            left_side += num
            
        return -1

obj = Solution()
print(obj.pivotIndex(nums = [1,7,3,6,5,6]))
