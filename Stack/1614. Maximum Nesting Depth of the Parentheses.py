class Solution:
    def maxDepth(self, s):
        maximum = 0
        count = 0

        for current in s:
            if current=='(':
                count += 1
            if current == ')':
                count -= 1
            
            maximum = max(maximum, count)
            print(maximum)
        
obj = Solution()
obj.maxDepth(s = "()(())((()()))")

