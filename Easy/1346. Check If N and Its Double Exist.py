class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for digit in arr:
            if (digit*2 in seen) or (digit%2==0 and digit//2 in seen):
                return True
            seen.add(digit)
        return False

obj = Solution()
ans = obj.checkIfExist(arr = [10,2,5,3])
print("Answer is: ", ans)