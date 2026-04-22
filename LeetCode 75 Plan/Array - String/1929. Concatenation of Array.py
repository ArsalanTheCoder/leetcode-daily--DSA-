# 1
class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans
#  2   
# class Solution:
#     def getConcatenation(self, nums):
#        return nums+nums

# 3
# class Solution:
#     def getConcatenation(self, nums):
#         ans =[]
#         n = len(nums)
#         for i in range(n):
#             ans[i]=nums[i]

#         for i in range(n):
#             ans[i+n] = nums[i]
#             print(ans)
        
#         return ans

# obj = Solution()
# print(obj.getConcatenation([1,2,3]))