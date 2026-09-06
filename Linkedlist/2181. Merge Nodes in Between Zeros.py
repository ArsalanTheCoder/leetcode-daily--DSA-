class ListNode:
    def __init__(self, val, next=next):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def mergeNodes(self, head):
        dummy = ListNode(0)
        tail = dummy
        current = head.next
        total = 0
        while current:
            if current.val !=0:
                total += current.val
            else:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0

            current = current.next
        return dummy.next

    def printList(self, dummy):
        current = dummy
        while current:
            print(current.val, end = "->")
            current = current.next
        print("None")

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(0)
node4 = ListNode(3)
node5 = ListNode(0)
node6 = ListNode(2)
node7 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

obj = Solution()
obj.head = node1

dummy = obj.mergeNodes(obj.head)
obj.printList(dummy)