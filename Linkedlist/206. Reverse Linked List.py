class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head):
        #current pointer
        current = head
        #previous pointer
        prev = None

        #while loop until current is None
        while current:
            #store current next node into temporary variable
            nextNode = current.next
            #Link the current node with previous pointer
            current.next = prev
            #Point the prevoius pointer to the first node
            prev = current
            #Move current node forward by putting nextNode into current pointer
            current = nextNode
        return prev

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
obj.printList(obj.head)
print()
obj.head = obj.reverseList(obj.head)
obj.printList(obj.head)



