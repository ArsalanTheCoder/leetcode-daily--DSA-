from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):

        # Step 1: Push new element into queue2
        self.queue2.append(x)

        # Step 2: Move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        # Step 3: Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not self.queue1

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.top())
print(obj.empty())
