from collections import Counter

class Solutoin:
    def findLHS(self, list):

        ans = 0
        freq = Counter(list)
        for x in freq:
            if x+1 in freq:
                ans = max(ans, freq[x]+freq[x+1])
        return ans

            

obj = Solutoin()
result = obj.findLHS([1,2,3,4])
print(result)