class Solution:
    def intersection(self, nums1, nums2):
        result = set()
        for num in nums1:
            if num in nums2:
                if num not in result:
                   result.add(num)
        return list(result)


obj = Solution()
ans=obj.intersection(nums1 = [1,2,2,1], nums2 = [2,2])
print(ans)
                        