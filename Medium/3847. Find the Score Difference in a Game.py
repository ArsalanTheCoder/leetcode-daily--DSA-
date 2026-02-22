class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        difference = 0
        is_p1_active = True  # True means Player 1, False means Player 2
        
        for i in range(len(nums)):
            
            # Rule 1: Is the number odd?
            if nums[i] % 2 != 0:
                is_p1_active = not is_p1_active  # Swap roles!
                
            # Rule 2: Is it the 6th game? (Indices 5, 11, 17...)
            # The remainder of dividing 5, 11, or 17 by 6 is always 5.
            if i % 6 == 5:
                is_p1_active = not is_p1_active  # Swap roles again!
                
            # Rule 3: Award the points to the active player
            if is_p1_active:
                # Player 1 gets points (pulls positive)
                difference += nums[i]
            else:
                # Player 2 gets points (pulls negative)
                difference -= nums[i]
                
        # The ribbon's final position is the exact difference!
        return difference

obj = Solution()
print(obj.scoreDifference(nums = [2,4,2,1,2,1]))