class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zeros_count+=1
            
            while zeros_count>k:
                if nums[left]==0:
                    zeros_count-=1
                left+=1

            max_len = max(max_len, right-left+1)
            
        return max_len
    
obj = Solution()
print(obj.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
                

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0
#         max_len = 0
#         zeros_count = 0
        
#         # Iterate with the right pointer
#         for right in range(len(nums)):
#             # If we see a zero, count it (use up one 'k')
#             if nums[right] == 0:
#                 zeros_count += 1
            
#             # If we have more than k zeros, our window is invalid.
#             # We must shrink it from the left until zeros_count <= k.
#             while zeros_count > k:
#                 # If the element leaving the window was a zero, we get a 'k' back
#                 if nums[left] == 0:
#                     zeros_count -= 1
#                 left += 1
            
#             # Update the max length
#             # The window size is always right - left + 1
#             max_len = max(max_len, right - left + 1)
            
#         return max_len                