class Solution:
    def finalPrices(self, prices):
    
    #First Approach without using stack
        # lst = []
        # n = len(prices)
        # for i in range(n):
        #     j = i+1 
        #     discount_found = False

        #     while j < n:
        #         if prices[j]<=prices[i]:
        #             lst.append(prices[i]-prices[j])
        #             discount_found = True
        #             break
        #         j+=1
            
        #     if not discount_found: 
        #         lst.append(prices[i])
        # return lst
    
    # Second Approach by using Stack

        stack = []
        for i,p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                index = stack.pop()
                prices[index] -= p
                
            stack.append(i)
        return prices  


obj = Solution()
answer = obj.finalPrices(prices = [8,4,6,2,3])
print(answer)