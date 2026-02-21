class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 1. Edge Case: All numbers are >= 1. 
        # If k is 0 or 1, the product can never be strictly less than k.
        if k <= 1:
            return 0
        
        product = 1
        count = 0
        left = 0
        
        # 2. Expand the window by moving the 'right' pointer
        for right in range(len(nums)):
            
            # Multiply the new number entering the window
            product *= nums[right]
            
            # 3. Shrink the window if the product gets too big
            while product >= k:
                # Divide out the number leaving the window
                product //= nums[left] 
                # Move the left pointer forward
                left += 1
                
            # 4. The "Magic" Counting Step
            # Add the number of valid subarrays that end at the current 'right' position
            count += right - left + 1
            
        return count
    
obj = Solution()
print(obj.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))