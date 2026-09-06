class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        total = m*n
        k = k%total

        ans = [ [0]*n for _ in range(m) ]

        for row in range(m):
            for col in range(n):

                index = (row * n)+col
                newIndex = (index+k) % total

                newRow = newIndex // n
                newCol = newIndex % n

                ans[newRow][newCol] = grid[row][col]
        
        return ans


obj = Solution()
ans = obj.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4)
print(ans)