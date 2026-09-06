# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        while True:
            smallest_index = -1

            # Find the list having the smallest current value
            for i in range(len(lists)):
                if lists[i] is not None:
                    if smallest_index == -1 or lists[i].val < lists[smallest_index].val:
                        smallest_index = i

            # All lists are finished
            if smallest_index == -1:
                break

            # Add the smallest node
            current.next = lists[smallest_index]
            current = current.next

            # Move that list forward
            lists[smallest_index] = lists[smallest_index].next

        return dummy.next
        
        