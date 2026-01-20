class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        a = len(word1)
        b = len(word2)
        length = max(a,b)

        for i in range(length):
            if i<a:
                result.append(word1[i])
            if i<b:
                result.append(word2[i])
        return  ''.join(result)

# 2nd Approach
# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         result = []
#         # 1. Find the length of the shorter word
#         n = min(len(word1), len(word2))
        
#         # 2. Iterate only through the common length (No 'if' checks needed!)
#         for i in range(n):
#             result.append(word1[i])
#             result.append(word2[i])
            
#         # 3. Add the leftovers (Slicing)
#         # If word1 is longer, this adds the rest. If not, it adds nothing.
#         result.append(word1[n:]) 
#         result.append(word2[n:])
        
#         return "".join(result)


obj = Solution()
obj.mergeAlternately(word1 = "abcd", word2 = "pq")