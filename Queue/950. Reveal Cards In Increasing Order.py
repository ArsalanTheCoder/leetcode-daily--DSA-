from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        dq = deque()
        print(deck)

        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(card)
        
        return list(dq)
    
obj = Solution()
ans = obj.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7])
print(ans)