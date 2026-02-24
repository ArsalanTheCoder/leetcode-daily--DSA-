class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = []
        answer2 = []

        # Loop through the SETS to guarantee distinct numbers
        for number in set1:
            if number not in set2:
                answer1.append(number)
        
        for number in set2:
            if number not in set1:
                answer2.append(number)
            
        # Return them wrapped in a single list
        return [answer1, answer2]

obj = Solution()
print(obj.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))