class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_area = 0

        while left<right:
            width = right-left
            Current_height = min (height[left], height[right])

            current_area = width * Current_height

            if current_area > max_area:
                max_area = current_area
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        
        return max_area
    

obj = Solution()
print(obj.maxArea(height = [1,8,6,2,5,4,8,3,7]))

# Dry Run Example: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Start: left (1), right (7). Width 8. Min Height 1. Area 8. (Move Left).
# Next: left (8), right (7). Width 7. Min Height 7. Area 49. (Move Right).
# Next: left (8), right (3). Width 6. Min Height 3. Area 18. (Move Right). ... and so on.
# The maximum area found will be 49.