class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        # Step 1: Calculate Left Products (Prefix)
        # We start with 1 because there is nothing to the left of the first element.
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i] # Update running product for the next person
            
        # Current state of 'answer' for input [1, 2, 3, 4]:
        # [1, 1, 2, 6] -> These are the products of everything to the left
        
        # Step 2: Calculate Right Products (Suffix) and multiply
        right_product = 1
        for i in range(n - 1, -1, -1): # Loop backwards
            answer[i] *= right_product # Multiply valid left product by right product
            right_product *= nums[i]   # Update running product for the next person
            
        return answer

obj = Solution()
print(obj.productExceptSelf( nums = [1,2,3,4]))