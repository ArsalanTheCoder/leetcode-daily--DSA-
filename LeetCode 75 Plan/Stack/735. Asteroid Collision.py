class Solution:
    def asteroidCollision(self, nums):
        Stack  = []
        
        for asteriod in nums:
            while Stack and asteriod < 0 and Stack[-1] > 0:
                if Stack[-1] < -asteriod:
                    Stack.pop()
                    continue
                elif Stack[-1] == -asteriod:
                    Stack.pop()
                break
            else:
                Stack.append(asteriod)
        
        return Stack


obj = Solution()
print(obj.asteroidCollision([5,10,-5, -14]))