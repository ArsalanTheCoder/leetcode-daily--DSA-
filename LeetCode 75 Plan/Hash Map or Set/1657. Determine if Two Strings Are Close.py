from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Quick check: If lengths are different, they can't be close
        if len(word1) != len(word2):
            return False
            
        # Rule 1: Do they have the exact same unique letters?
        if set(word1) != set(word2):
            return False
            
        # Rule 2: Do they have the exact same frequency patterns?
        # We get the counts, sort them from smallest to largest, and compare!
        counts1 = sorted(Counter(word1).values())
        counts2 = sorted(Counter(word2).values())
        
        return counts1 == counts2

obj = Solution()
print(obj.closeStrings(word1 = "abc", word2 = "bca"))

