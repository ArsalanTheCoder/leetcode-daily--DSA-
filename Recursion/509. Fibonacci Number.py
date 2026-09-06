class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)


obj = Solution()
result = obj.fib(5)
print(result)



# # 🔥 Recursion | Fibonacci Number | LeetCode 509

# ### Approach
# Use the recursive definition of Fibonacci:

# - `F(0) = 0`
# - `F(1) = 1`
# - `F(n) = F(n-1) + F(n-2)`

# The base cases stop the recursion, while the recursive case breaks the problem into smaller subproblems.

# ### Complexity

# - **Time:** `O(2^n)`
# - **Space:** `O(n)` — recursion call stack

# ### Code

# ```python
# class Solution:
#     def fib(self, n):
#         if n == 0:
#             return 0

#         if n == 1:
#             return 1

#         return self.fib(n - 1) + self.fib(n - 2)