class Solution:
    def numberOfSubarrays(self, nums, k):

        # Count subarrays with at most k odd numbers
        def atMost(k):
            left = 0
            ans = 0

            for right in range(len(nums)):

                # Reduce remaining odd limit
                if nums[right] % 2 == 1:
                    k -= 1

                # Shrink window if odd count exceeds limit
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1

                # Count all valid subarrays ending at 'right'
                ans += right - left + 1

            return ans

        # Exactly k = AtMost(k) - AtMost(k-1)
        return atMost(k) - atMost(k - 1)

obj = Solution()
result = obj.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
print(result)

# later do dry run on this same input