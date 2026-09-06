class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words)!=len(pattern):
            return False

        charToWords = {}
        wordsToChar = {}

        for ch, word in zip(pattern, words):
            if ch in charToWords:
                if charToWords[ch]!=word:
                    return False
            else:
                charToWords[ch] = word

            if word in wordsToChar:
                if wordsToChar[word]!=ch:
                    return False
            else:
                wordsToChar[word] = ch

        return True
         

obj = Solution()
print(obj.wordPattern(pattern = "abba", s = "dog cat  cat dog"))