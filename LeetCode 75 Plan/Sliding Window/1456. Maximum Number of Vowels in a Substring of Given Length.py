class Solution(object):
    def maxVowels(self, s, k):
        # Using a set is slightly faster for lookups
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        count = 0
        # Build first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        max_count = count
        
        # Slide the window
        for i in range(k, len(s)):
            # Optimization: Early exit if we found the max possible
            if max_count == k:
                return k
            
            # Remove element leaving
            if s[i - k] in vowels:
                count -= 1
            # Add element entering
            if s[i] in vowels:
                count += 1
            
            if count > max_count:
                max_count = count
                
        return max_count

# Test run
obj = Solution()
# "leetcode" has vowels: e, e, o, e (Total 4)
print(obj.maxVowels(s="leetcode", k=8)) # Output: 4