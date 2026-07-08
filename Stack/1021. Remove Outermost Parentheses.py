class Solution:
    def removeOuterParentheses(self, s):
        depth = 0
        stack=[]
        
        for ch in s:
            if ch=='(':
                if depth>0:
                    stack.append(ch)
                depth+=1
            elif ch == ')':
                depth-=1
                if depth>0:
                    stack.append(ch)

        return (''.join(stack))

obj = Solution()
result = obj.removeOuterParentheses( s = "(()())(())(()(()))")
print(result)