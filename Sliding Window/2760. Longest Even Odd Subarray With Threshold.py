class Solution:
    def longestAlternatingSubarray(self, nums, threshold):
        ans = 0
        current = 0

        for i in range(len(nums)):

            # Start a new subarray
            if current == 0:
                if nums[i] % 2 == 0 and nums[i] <= threshold:
                    current = 1
                    ans = max(ans, current)

            # Try to extend the current subarray
            else:
                if nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                    current += 1
                    ans = max(ans, current)
                else:
                    # Start a new subarray from the current element if possible
                    if nums[i] % 2 == 0 and nums[i] <= threshold:
                        current = 1
                    else:
                        current = 0

        return ans

obj = Solution()
ans = obj.longestAlternatingSubarray(nums = [1], threshold = 4)
print(ans)