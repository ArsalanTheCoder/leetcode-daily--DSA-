class Solution:
    def getConcatenation(self, nums):
        ans =[]
        n = len(nums)
        for i in range(n):
            ans[i]=nums[i]

        for i in range(n):
            ans[i+n] = nums[i]
            print(ans)
        
        return ans

obj = Solution()
print(obj.getConcatenation([1,2,3]))