from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        queue = deque()

        time  = 0
        for i in range(len(tickets)):
            queue.append([i, tickets[i]])
        print(queue)

        while queue:
            person = queue.popleft()
            person[1]-=1
            time+=1
            if person[1]==0:
                if person[0]==k:
                    return time
            
            if person[1]>0:
                queue.append(person)
            

    
obj = Solution()
result = obj.timeRequiredToBuy(tickets = [5,1,1,1], k = 0)
print(result)