# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head                 # start of odd list
        even = head.next           # start of even list
        even_head = even           # to connect later

        # rearrange pointers
        while even and even.next:
            odd.next = even.next   # link next odd
            odd = odd.next

            even.next = odd.next   # link next even
            even = even.next

        # connect odd list with even list
        odd.next = even_head

        return head
    