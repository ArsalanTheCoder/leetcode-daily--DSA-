class Solution:
    def maxDepth(self, s):
        maximum = 0
        count = 0

        for current in s:
            if current=='(':
                count += 1
            elif current == ')':
                count -= 1
            
            maximum = max(maximum, count)
        
        return maximum
        
obj = Solution()
obj.maxDepth(s = "()(())((()()))")

