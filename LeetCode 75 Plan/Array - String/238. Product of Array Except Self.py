class Solution(object):
    def productExceptSelf(self, nums):
        lst = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    continue
                result *= nums[j]
            lst.append(result)
        print(lst)


obj = Solution()
obj.productExceptSelf(nums = [-1,1,0,-3,3])
# i will tomorrow