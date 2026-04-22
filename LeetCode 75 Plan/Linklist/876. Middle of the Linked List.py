class listNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    

class Solution:
    def middleNode(self, head):
        slow = head
        fast  = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp=temp.next
    print("None")

head = listNode(1)
head.next = listNode(2)
head.next.next = listNode(3)
head.next.next.next = listNode(4)
head.next.next.next.next = listNode(5)

obj = Solution()
obj.middleNode(head)
printList(head)
updated_head=obj.middleNode(head)
printList(updated_head)



