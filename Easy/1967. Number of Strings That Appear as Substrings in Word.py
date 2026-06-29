class Solution:
    def numOfStrings(self, patterns, word):
        counter = 0
        for i in patterns:
            if i in word:
                counter+=1
        return counter

obj = Solution()
ans = obj.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc")
print(ans)