# By using iterative(loop-based) or Brute-Force approach
# class Solution:
#     def kthCharacter(self, k):
#         lst1 = [97]
#         print(lst1)
#         while len(lst1) < k:
#             old_length = len(lst1)
#             for i in range(old_length):
#                 digit = lst1[i]
#                 digit += 1
#                 lst1.append(digit)

#         return chr(lst1[k-1])


#By using Recursive Approach
class Solution:
    def kthCharacter(self, k):
        lst = [97]

        def build( length):
            if len(lst)>=k:
                return
            for i in range(length):
                lst.append(lst[i]+1)

            return len(lst)

        build(1)
        return chr(lst[k-1])
        

obj = Solution()
obj.kthCharacter(10)