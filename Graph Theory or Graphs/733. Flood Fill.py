class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(row, col):
            if row<0 and row>=len(image):
                return
            
            if col<0 and col>=len(image[0]):
                return
            if image[row][col] != original_color:
                return

            image[row][col] = color

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        dfs(sr, sc)

        return image


obj = Solution()
answer = obj.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(answer)