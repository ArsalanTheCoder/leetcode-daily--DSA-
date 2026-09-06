class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Create Nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

# Connect Nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Uncomment to create a cycle
node4.next = node2

obj = Solution()
print(obj.hasCycle(node1))