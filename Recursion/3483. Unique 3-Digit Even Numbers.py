# class Solution:
#     def totalNumbers(self, digits: List[int]) -> int:
#         n = len(digits)
#         result = set()
#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):
#                     if i!=j and i!=k and j!=k:
#                         if digits[i] != 0:
#                             if digits[j]%2 == 0:
#                                 num = digits[i]*100 + digits[j]*10 + digits[k]
#                                 result.add(num)
#         return len(result)

                            
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        result = set()

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    if i == j or i == k or j == k:
                        continue

                    if digits[i] == 0:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    result.add(num)

        return len(result)



# # 🔥 Simple Brute Force | 3 Digits + Set | LeetCode 3483

# # Intuition

# Try every possible combination of 3 different digit copies and use a `set` to store only unique valid numbers.

# # Approach

# - Use three loops for the hundreds, tens, and ones positions.
# - Make sure the same index is not reused.
# - The first digit cannot be `0`.
# - The last digit must be even.
# - Store each valid number in a `set` to remove duplicates.
# - Return the size of the set.

# # Complexity

# - **Time Complexity:** `O(n³)`
# - **Space Complexity:** `O(m)`, where `m` is the number of distinct valid numbers.

# # Code

# ```python
# class Solution:
#     def totalNumbers(self, digits: List[int]) -> int:
#         n = len(digits)
#         result = set()

#         for i in range(n):
#             for j in range(n):
#                 for k in range(n):

#                     if i == j or i == k or j == k:
#                         continue

#                     if digits[i] == 0:
#                         continue

#                     if digits[k] % 2 != 0:
#                         continue

#                     num = digits[i] * 100 + digits[j] * 10 + digits[k]
#                     result.add(num)

#         return len(result)    