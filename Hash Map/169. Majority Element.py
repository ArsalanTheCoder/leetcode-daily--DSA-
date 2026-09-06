class Solution:
    def majorityElement(self, nums):
        freq = {}
        large = 0
        n = len(nums)/2
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
            large = max(large, freq[num])
            if large > n:
                print("yes")
                return num
        
obj = Solution()
result = obj.majorityElement(nums = [2,2,1,1,1,2,2])
print(result)