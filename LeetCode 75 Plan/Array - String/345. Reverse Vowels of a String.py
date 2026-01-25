class Solution(object):
    def reverseVowels(self, s):
        # Step 1: Convert to list so we can modify it
        s = list(s)
        length = len(s)
        
        # IMPROVEMENT: Use a set {} instead of a list []. 
        # Sets are much faster for checking "in" logic.
        seen = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        left = 0
        right = length - 1
        
        while left < right: # '<' is enough, no need for '<=' (swapping same letter is useless)
            
            # Case 1: Left pointer is NOT at a vowel -> Move it forward
            if s[left] not in seen:
                left += 1
            
            # Case 2: Right pointer is NOT at a vowel -> Move it backward
            # Note: We use 'elif' so we only move one pointer at a time
            elif s[right] not in seen:
                right -= 1
            
            # Case 3: Both are vowels -> SWAP them!
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        # CRITICAL FIX: Return the string, don't print it!
        return "".join(s)

# Test it
obj = Solution()
print(obj.reverseVowels("leetCode")) 
# Output: "leotCede"