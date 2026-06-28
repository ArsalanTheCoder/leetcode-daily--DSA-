class Solution:
    def maximumStrongPairXor(self, nums):
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                x = nums[i]
                y = nums[j]
                if abs(x-y) <= min(x,y):
                    ans = max(ans, x^y)
        return ans
    
obj = Solution()
result = obj.maximumStrongPairXor(nums = [1,2,3,4,5])
print(result)