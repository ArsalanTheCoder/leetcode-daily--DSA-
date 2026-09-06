class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prevGroup = dummy

        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            nextGroup = kth.next
            current = prevGroup.next
            prev = nextGroup

            while current != nextGroup:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

    def printList(self, head):
        current = head
        while current:
            print(current.val, end="->")
            current = current.next
        print("None")


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
node1.next.next.next.next = ListNode(5)

obj = Solution()
obj.head = node1
obj.printList(obj.head)
result = obj.reverseKGroup(obj.head, 2)
obj.printList(result)




# # 🔄 Reverse Nodes in k-Group | O(n) Time | O(1) Space

# ### Approach
# - Find the `kth` node of each group.
# - Reverse exactly `k` nodes in-place.
# - Connect the reversed group with the previous group.
# - Leave the remaining nodes unchanged if fewer than `k` nodes remain.

# ### Complexity
# - **Time:** `O(n)`
# - **Space:** `O(1)`

# ### Key Concept
# Use `groupPrev`, `kth`, and `nextGroup` pointers to control each group without creating extra nodes.

# ```python
# class Solution:
#     def reverseKGroup(self, head, k):
#         dummy = ListNode(0)
#         dummy.next = head
#         prevGroup = dummy

#         while True:
#             kth = prevGroup

#             for _ in range(k):
#                 kth = kth.next
#                 if kth is None:
#                     return dummy.next

#             nextGroup = kth.next
#             current = prevGroup.next
#             prev = nextGroup

#             while current != nextGroup:
#                 nextNode = current.next
#                 current.next = prev
#                 prev = current
#                 current = nextNode

#             temp = prevGroup.next
#             prevGroup.next = kth
#             prevGroup = temp