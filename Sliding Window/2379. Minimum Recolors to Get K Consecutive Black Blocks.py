# My approach to solve this question.
# from collections import Counter
# class Solution:
#     def minimumRecolors(self, blocks, k):
#         left = 0
#         window = blocks[left:k]
#         freq=Counter(window)
#         whiteColor = freq["W"]

#         ans = whiteColor
#         print(ans)

#         for right in range(k, len(blocks)+1):
#             left+=1
#             window = blocks[left:right]
#             freq=Counter(window)
#             whiteColor = freq["W"]
#             ans = min(ans, whiteColor)
#             print(window)
        
#         return ans
        

class Solution:
    def minimumRecolors(self, blocks, k):
        white = 0

        for i in range(k):
            if blocks[i]=="W":
                white+=1
            
        ans = white    
        n = len(blocks) 
        for right in range(k,n):
            if blocks[right-k]=='W':
                white-=1
            
            if blocks[right]=='W':
                white+=1
            
            ans = min(ans, white)
        
        return ans




obj = Solution()
answer = obj.minimumRecolors(blocks = "WWBBBWBBBBBWWBWWWB", k = 16)
# print(answer)