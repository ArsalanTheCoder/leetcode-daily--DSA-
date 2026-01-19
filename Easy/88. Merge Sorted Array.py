class Solution(object):
    def merge(self, nums1, nums2, m, n):
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        print(nums1)


obj = Solution()
obj.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
#solve with another method soon by below see:

        # p1 = m-1
        # p2 = n-1
        # p = m+n-1
        # while p2 >=0: 
        #     if p1>=0 and nums1[p1]>nums2[p2]:
        #         nums1[p]=nums1[p1]
        #         p1-=1
        #     else:
        #         nums1[p]=nums2[p2]
        #         p2-=1
        #     p-=1