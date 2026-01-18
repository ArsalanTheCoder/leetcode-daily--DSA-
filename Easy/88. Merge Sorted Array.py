class Solution(object):
    def merge(self, nums1, nums2, m, n):
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        print(nums1)


obj = Solution()
obj.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)