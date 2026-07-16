class Solution:
    def maximumMex(self, nums):
        result = []

        for k in range(1, len(nums)+1):
            prefix = nums[:k]
            s = set(prefix)
            mex = 0
            while mex in s:
                mex+=1
            result.append(mex)
        print(result)

obj = Solution()
ans = obj.maximumMex(nums = [1,0,2])
# i will solve it later
