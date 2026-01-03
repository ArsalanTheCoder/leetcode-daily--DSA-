# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Solution 1
# class Solution(object):
#     def isPalindrom(self, number):
#         if number <= 0:
#             return False
#         s = str(number)
#         return s==s[::-1]
# Complexity
# Time: O(n)
# Space: O(n)

#Solution 2
# class Solution(object):
#     def isPalindrom(self, number):
#         if number < 0:
#             return False
#         s = str(number)
#         left = 0
#         right = len(s)-1
#         while left<right:
#             if s[left]!=s[right]:
#                 return False
#             left +=1
#             right -=1
#         return True
# Complexity
# Time: O(n)
# Space: O(n)    

#Solution 3
class Solution(object):
    def isPalindrom(self, number):
        if number<0:
            return False
        original_Number = number
        reverse_Number = 0

        while number > 0:
            rem = number % 10
            reverse_Number = reverse_Number*10 + rem
            number = number//10
        return original_Number == reverse_Number
# Complexity
# Time: O(n)
# Space: O(1) 


obj = Solution()
print(obj.isPalindrom(121))        
#Done
