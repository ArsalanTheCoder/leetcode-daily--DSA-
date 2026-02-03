class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()  # Step 1: Sort the array
        
        left = 0
        right = len(nums) - 1
        count_max = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                # Found a pair! Move both pointers inward
                count_max += 1
                left += 1
                right -= 1
            elif current_sum < k:
                # Sum is too small, need larger numbers -> Move Left forward
                left += 1
            else: # current_sum > k
                # Sum is too big, need smaller numbers -> Move Right backward
                right -= 1
                
        return count_max

obj = Solution()
s= obj.maxOperations(nums = [3,1,3,4,2,4,5,3], k = 6)
print(s) 
