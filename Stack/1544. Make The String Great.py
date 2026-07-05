class Solution:
    def makeGood(self, s):
        stack = []

        for i in range(len(s)):

            if stack and (s[i].lower() == stack[-1].lower()):
                if s[i]!=stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            print(stack)
        return ''.join(stack)

obj = Solution()
answer = obj.makeGood(s = "leEeetcode")


