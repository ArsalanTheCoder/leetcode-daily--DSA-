class Solution(object):
    def reverseWords(self, s):
        # Step 1: Clean up spaces and split into list
        words = s.split() 
        
        # Step 2: Two Pointers to swap
        left = 0
        right = len(words) - 1
        
        while left < right: # < is enough, no need to swap middle element with itself
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
            
        # Step 3: Join back into a string and RETURN
        return ' '.join(words)

#Second Solution
# class Solution(object):
#     def reverseWords(self, s):
#         # s.split() -> breaks into words
#         # [::-1] -> reverses the list instantly
#         # ' '.join -> puts them back together
#         return ' '.join(s.split()[::-1])


obj = Solution()
obj.reverseWords(s = "a good   example")



# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # Step 1: Split string into words (removes extra spaces automatically)
#         s_split = s.split()
        
#         # Step 2: Reverse the list using slicing
#         reverse_s = s_split[::-1]
        
#         # Step 3: Join back with a single space
#         return ' '.join(reverse_s)