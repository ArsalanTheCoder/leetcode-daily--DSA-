# class Solution(object):
#     def isSubsequence(self, s, t):
#         s_pointer = 0
#         for i in range(len(t)):
#             if s_pointer<len(s) and s[s_pointer]==t[i]:
#                 s_pointer+=1

#         if s_pointer < len(s):
#             return False
#         else:
#             return True

#Second Solution
class Solution(object):
    def isSubsequence(self, s, t):
        # Handle empty s edge case immediately (Empty string is always a subsequence)
        if not s: return True
        
        s_pointer = 0
        s_len = len(s)
        
        for char in t:
            # If we found the current needed character
            if s_pointer < s_len and char == s[s_pointer]:
                s_pointer += 1
                
                # OPTIMIZATION: If we found all characters, stop early!
                if s_pointer == s_len:
                    return True
                    
        # If loop finishes without finding everything
        return s_pointer == s_len

        
obj = Solution()
print(obj.isSubsequence( s = "axc", t = "ahbgdc"))