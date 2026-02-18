class Solution:
    def containsNearbyDuplicate(self, nums, k):
        # A set to keep track of the numbers in our current window
        window = set()
        
        for i in range(len(nums)):
            # 1. Check if the current number is already in our window
            if nums[i] in window:
                return True
            
            # 2. Add the current number to the window
            window.add(nums[i])
            
            # 3. Maintain the window size
            # If the window is bigger than k, remove the oldest element (the one at i - k)
            if len(window) > k:
                window.remove(nums[i - k])
                
        # If we finish the loop without finding a match
        return False
    

obj = Solution()
print(obj.containsNearbyDuplicate(nums = [1,2,3,7,1], k = 3))  