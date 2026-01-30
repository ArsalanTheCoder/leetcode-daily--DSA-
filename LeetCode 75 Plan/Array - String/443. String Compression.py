class Solution(object):
    def compress(self, chars):
        write = 0 # write operator that insert the compressed result
        read = 0 # read pointer that scan the complete array

        # Step 1: First Loop that scan the array one by one
        while read < len(chars):
            current_char = chars[read]
            count = 0
        
        # Step 2: Second loop that count the consecutive or duplicate characters
            while read < len(chars) and current_char == chars[read]:
                count += 1 # Count how many consecutive elements are present
                read += 1  # read pointer will reach where next character is present
            
        # Step 3: Insert the Current Character in the array (chars)
            chars[write] = current_char
            write += 1
        
        # Step 4: If count > 1 then we insert the how many current characters are there, Otherwise just Current character
            if count > 1:
                for digits in str(count):
                    chars[write] = digits
                    write += 1

        return write


    

obj = Solution()
a=obj.compress(chars = ["a","a","b","b","c","c","c"])
print(a)
