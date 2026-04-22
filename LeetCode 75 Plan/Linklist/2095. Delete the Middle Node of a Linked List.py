class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        
        # Count length
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        # Find middle
        middle = count // 2
        
        # Go to node before middle
        temp = head
        for _ in range(middle - 1):
            temp = temp.next
        
        # Delete middle node
        temp.next = temp.next.next
        
        return head


# 🔥 Helper function to print list
def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")



# 🔥 Create Linked List: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 🔥 Call function
obj = Solution()
new_head = obj.deleteMiddle(head)

# 🔥 Print result
printList(new_head)