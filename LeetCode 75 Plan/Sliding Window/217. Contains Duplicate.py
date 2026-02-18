class Solution:
    def containsDuplicate(self, nums):
        # Create a set to store unique elements
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate!
            if num in seen:
                return True
            # Otherwise, add it to the set
            seen.add(num)
            
        # If we finish the loop, no duplicates were found
        return False
    

obj = Solution()
print(obj.containsDuplicate(nums = [1,2,3,7,1])) 