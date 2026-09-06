class Solution:
    def maxProduct(self, nums):
        maximum = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                ans = (nums[i]-1)*(nums[j]-1)
                maximum = max(maximum, ans)
        return maximum

obj = Solution()
result = obj.maxProduct(nums = [3,7])
print(result)