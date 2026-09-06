class Solution:
    def isPowerTwo(self, n):
        i = 0
        p = self.handler(i, n)
        print("Answer: ", p)

    def handler(self, i, n):
        value = 2**i
        if value == n:
            return True
        if value > n:
            return False
        return self.handler(i+1, n)

obj = Solution()
obj.isPowerTwo(1)
obj.isPowerTwo(16)
obj.isPowerTwo(3)
obj.isPowerTwo(128)


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and (n & (n - 1)) == 0
    