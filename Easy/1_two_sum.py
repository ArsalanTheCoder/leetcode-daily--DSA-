class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for index, value in enumerate(numbers):
            dif = target-value
            if dif in seen:
                return [seen[dif],index]
            seen[value] = index


obj = Solution()
print(obj.twoSum([2,7,11,15],9))