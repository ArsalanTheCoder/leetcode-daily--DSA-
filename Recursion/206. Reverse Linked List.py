class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head):
        prev = None
        current = head
        return self.helper(current, prev)

    def helper(self, current, prev):
        if current is None:
            return prev

        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

        return self.helper(current, prev)

    def printList(self, head):
        dummy = head
        while dummy:
            print(dummy.val, end="->")
            dummy = dummy.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

obj = Solution()
obj.head = node1

print("Before Reversing:")
obj.printList(obj.head)

obj.head = obj.reverseList(obj.head)

print("After Reversing:")
obj.printList(obj.head)

# see tomorrow
# class Solution:
#     def reverseList(self, head):

#         # Base case
#         if head is None or head.next is None:
#             return head

#         # Reverse the rest of the list
#         newHead = self.reverseList(head.next)

#         # Put current node after its next node
#         head.next.next = head

#         # Remove old forward connection
#         head.next = None

#         return newHead