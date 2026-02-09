class Solution:
    def minRemoval(self, nums, k) :
        # Step 1: Line everyone up!
        nums.sort()  
        
        n = len(nums)   # Total number of players
        max_kept = 0    # The biggest group we have found so far
        left = 0        # The start of our "frame" (index of the smallest number in current group)
        
        # Step 2: Slide the 'right' side of the frame forward one by one
        for right in range(n):
            
            # Step 3: Check the Rule
            # nums[right] is the biggest in our current frame.
            # nums[left] is the smallest in our current frame.
            # If (Biggest > Smallest * k), the group is invalid.
            while nums[right] > nums[left] * k:
                # The group is invalid! We must shrink the frame from the left.
                # We drop the smallest number (increment left) to try and fix the balance.
                left += 1
            
            # Step 4: The group is now valid. Calculate its size.
            current_window_size = right - left + 1
            
            # Step 5: Is this the biggest group we've seen? Remember it.
            if current_window_size > max_kept:
                max_kept = current_window_size
                
        # Step 6: The Answer
        # Total players - (Max players we can keep) = (Min players to remove)
        return n - max_kept

obj = Solution()
print(obj.minRemoval(nums = [1, 5, 2, 10], k = 3))