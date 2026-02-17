class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros_count = 0
        max_len = 0
        
        # Iterate through the array using 'right' as the end of the window
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            # If we have more than 1 zero, shrink window from the left
            while zeros_count > 1:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Why 'right - left' and not 'right - left + 1'?
            # The window size is (right - left + 1).
            # The problem forces us to delete exactly one element.
            # So the length of 1s is: (Window Size) - 1
            # (right - left + 1) - 1  ==  right - left
            max_len = max(max_len, right - left)
            
        return max_len

obj = Solution()
print(obj.longestSubarray(nums = [1,1,0,1]))