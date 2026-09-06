class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def middleNode(self, head):
        # Initialize two pointers, slow and fast
        slow = fast = head

        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow

    def printList(self):
        current = self.head
        while current:
            print(current.val, end = "->")
            current = current.next
        print("None")


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    obj = Solution()
    obj.head = node1

    middle_node = obj.head= obj.middleNode(obj.head)
    obj.printList()
    print("Middle Node Value:", middle_node.val)  # Output: Middle Node Value: 3