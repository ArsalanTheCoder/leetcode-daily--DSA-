class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.l1 = None
        self.l2 = None

    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        self.handler(current, l1, l2, carry)

        return dummy.next
    
    def handler(self, current, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry:
                current.next = ListNode(carry)
            return

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 +carry
        digit = total % 10
        carry = total // 10

        current.next = ListNode(digit)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        self.handler(current, l1, l2, carry)


node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)

obj = Solution()
obj.l1 = node1
obj.l2 = node2

obj.addTwoNumbers(obj.l1, obj.l2)



# # 🔥 LeetCode 2 — Add Two Numbers | Linked List + Carry

# ### Approach

# Traverse both linked lists together and add their digits along with the `carry`.

# - `total = val1 + val2 + carry`
# - `digit = total % 10`
# - `carry = total // 10`
# - Use a **dummy node** to build the result.
# - Continue while either list has nodes or a `carry` remains.

# ### Complexity

# - **Time:** `O(max(n, m))`
# - **Extra Space:** `O(1)` *(excluding the output list)*

# ### Code

# ```python
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:

#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry

#             digit = total % 10
#             carry = total // 10

#             current.next = ListNode(digit)
#             current = current.next

#             if l1:
#                 l1 = l1.next

#             if l2:
#                 l2 = l2.next

#         return dummy.next