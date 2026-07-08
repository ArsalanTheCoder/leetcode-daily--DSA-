class Solution:
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word

        stack = []
        idx = 0
        n = len(word)
        ans = []

        for i in range(n):
            if word[i] == ch:
                stack.append(word[i])
                idx = i
                break
            stack.append(word[i])

        for i in range(len(stack)-1, -1, -1):
            ans.append(stack[i])

        ans.append(word[idx+1:])

        return "".join(ans)
        
obj = Solution()
result = obj.reversePrefix(word = "abcd", ch = "d")
print(result)