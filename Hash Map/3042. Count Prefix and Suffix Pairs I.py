class Solution:
    def countPrefixSufixPairs(self, words):
        count  = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[j].endswith(words[i]) and words[j].startswith(words[i]):
                    count+=1

        return count


obj = Solution()
result = obj.countPrefixSufixPairs(words = ["pa","papa","ma","mama"])
print(result)