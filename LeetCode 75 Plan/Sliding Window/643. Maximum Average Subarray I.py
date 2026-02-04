class Solution(object):
    def findMaxAverage(self, nums, k):
        # 1. Use a clear name for the running sum
        current_sum = 0
        
        # 2. Use 'k' directly instead of len(nums[:k])
        for i in range(k):
            current_sum += nums[i]
            
        # Initialize Max with the sum of the first window
        Max = current_sum
        
        # 3. Iterate through the rest
        for j in range(k, len(nums)):
            # Slide window: subtract element leaving, add element entering
            current_sum -= nums[j-k]
            current_sum += nums[j]
            
            # Update Max if current window sum is larger
            if current_sum > Max:
                Max = current_sum
            
            # REMOVED: print(Max) -> This prevents Time Limit Exceeded
        
        # 4. Perform float division at the very end
        # In Python 3, / is always float division. 
        # In Python 2, you might need float(Max) / k to be safe.
        return Max / float(k)

# Test run
obj = Solution()
print(obj.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))