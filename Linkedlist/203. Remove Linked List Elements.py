class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class Solution:
    def removeElements(self, head, value):
        if head is None:
            return
        while head and  head.value ==value:
            head = head.next

        current = head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

        return head
