class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    # This is list a conversion approach.
    # def pairSum(self, head):
    #     if head is None:
    #         return 
    #     lst = []
    #     while head:
    #         lst.append(head.val)
    #         head = head.next

    #     n = len(lst)
    #     sum = maxSum = float('-inf')

    #     for i in range(n//2):
    #         index = (n-1-i)
    #         sum = lst[i]+lst[index]
    #         maxSum = max(maxSum, sum)
    #     return maxSum

    def pairSum(self, head):
        if head is None:
            return None
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current = slow
        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        first = head
        second = prev
        maxSum = float('-inf')

        while second:
            maxSum = max(maxSum, first.val + second.val)
            first = first.next
            second = second.next

        return maxSum



node1 = ListNode(4)
node1.next = ListNode(2)
node1.next.next = ListNode(2)
node1.next.next.next = ListNode(3)

obj = Solution()
obj.head = node1
result = obj.pairSum(obj.head)
print(result)




# Intuition
# Use Fast & Slow Pointers to find the middle of the linked list, reverse the second half, and then compare both halves to find the maximum twin sum.

# Approach
# Find the middle using slow and fast.
# Reverse the second half of the list.
# Compare corresponding nodes from both halves.
# Track the maximum twin sum.

# Complexity
# Time Complexity: O(n)
# Space Complexity: O(1)