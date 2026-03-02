class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                # Agar star aya, toh aakhri letter uda do
                stack.pop()
            else:
                # Agar normal letter hai, toh stack mein daal do
                stack.append(char)
                
        # Stack ko wapas join kar ke string bana do
        return "".join(stack)

obj = Solution()
print(obj.removeStars(s = "erase*****"))

#Techniques
# Agar letter * nahi hai, toh usko Stack (list) mein daal do.
# Agar letter * hai, toh Stack mein se aakhri letter nikal do (pop).
