from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)
        n = len(s2)
        
        # If s1 is bigger than s2, impossible to contain it
        if k > n:
            return False
        
        # Step 1: Count frequency of chars in s1
        # Example: s1="ab" -> count_s1 = {'a': 1, 'b': 1}
        count_s1 = Counter(s1)
        
        # Step 2: Create the first window in s2 (first k chars)
        window_count = Counter(s2[:k])
        
        # Check if the very first window is a match
        if count_s1 == window_count:
            return True
        
        # Step 3: Slide the window across s2
        for i in range(n - k):
            # 'i' is the character leaving the window
            # 'i + k' is the new character entering the window
            
            # Remove the old character (left side)
            start_char = s2[i]
            window_count[start_char] -= 1
            if window_count[start_char] == 0:
                del window_count[start_char] # Remove key if count is 0
            
            # Add the new character (right side)
            new_char = s2[i + k]
            window_count[new_char] += 1
            
            # Check for match
            if count_s1 == window_count:
                return True
                
        return False
    

obj = Solution()
res=obj.checkInclusion(s1 = "ab", s2 = "eidbaooo")
print(res)

