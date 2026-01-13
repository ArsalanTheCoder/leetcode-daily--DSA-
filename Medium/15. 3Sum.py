class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        lst = []
        for i in range(len(nums)):
            if i>0  and nums[i]==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    lst.append([nums[i],nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return lst




obj = Solution()
print(obj.threeSum( nums = [-1,-2,1,2,0]))