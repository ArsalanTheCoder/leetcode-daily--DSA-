from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        print(self.queue)
        return len(self.queue)

recentCounter = RecentCounter()

print(recentCounter.ping(1))
print(recentCounter.ping(100))
print(recentCounter.ping(3001))
print(recentCounter.ping(3002))