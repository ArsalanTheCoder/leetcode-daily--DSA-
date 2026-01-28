class Solution(object):
    def increasingTriplet(self, nums):
       # Start with infinit numbers so real number will replace them
        first = float('inf')
        second = float('inf')

        for n in nums:
            #Case 1: We found the smallest number
            if n<= first:
                first = n
            #Case 2: We found the second smallest number that is bigger than 'first' but smaller than second.
            elif n<= second:
                second = n
            #Case 3: We found the number that is bigger than both first and second
            # Since 'second' exists, we know a 'first' existed before it. 
            # So we have 1 -> 2 -> 3. Win!
            else:
                return True
        return False

obj = Solution()
print(obj.increasingTriplet(nums = [1,2,3,4,5]))