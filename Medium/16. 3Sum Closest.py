class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        print(nums)
        result = nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                currentSum = nums[i]+nums[left]+nums[right]
                if abs(target-currentSum) < abs(target-result):
                    result = currentSum
                if currentSum < target:
                    left +=1
                elif currentSum > target:
                    right -=1
                else:
                    return currentSum
        return result
    
obj = Solution()
print(obj.threeSumClosest( nums = [-1,2,3,4,-4], target = 2))