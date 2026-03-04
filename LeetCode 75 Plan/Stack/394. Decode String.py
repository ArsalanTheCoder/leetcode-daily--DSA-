class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Agar 2 ya 3 digit ka number ho (e.g., "12"), toh isliye * 10 karte hain
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # SAVE POINT: Purana data stack mein dalo aur variables reset karo
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
                
            elif char == ']':
                # RESOLVE POINT: Stack se purani cheezein nikalo aur multiply karo
                prev_str, num = stack.pop()
                current_str = prev_str + (current_str * num)
                
            else:
                # Normal letter hai, bas string mein add karte jao
                current_str += char
                
        return current_str
    
obj = Solution()
print(obj.decodeString(s = "3[a]2[bc]"))