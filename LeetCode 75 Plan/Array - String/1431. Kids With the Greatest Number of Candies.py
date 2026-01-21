class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxLen = max(candies)
        n = len(candies)
        lst = []
        for i in range(n):
            if candies[i]+extraCandies>=maxLen:
                lst.append(True)
            else:
                lst.append(False)
        return lst

obj = Solution()
print(obj.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))