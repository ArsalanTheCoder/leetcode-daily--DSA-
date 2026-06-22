class Solution:
    #First Soltion by simple approach
    # def A(self, iterate, k, code):
    #     if k==0:
    #         return 0
    #     total = 0
    #     n = len(code)
    #     for _ in range(abs(k)):
    #         if k>0:
    #             index = iterate % n
    #             total+=code[index]
    #             iterate+=1
    #         if k<0:
    #             index = (iterate-2) % n 
    #             total += code[index]
    #             iterate-=1
    #     return total

    # def decrypt(self, code, k):
    #     result = [0]*len(code)

    #     for i in range(len(code)):
    #         result[i]=self.A(i+1, k, code)
    #     return result 

    #Second Approach Sliding Window
    def decrypt(self, code, k):
        n = len(code)
        result = [0]*n
        if k==0:
            for i in range(n):
                result[i]=0
        elif k>0:
            left = 1
            right = k
            sum_window = sum(code[left:right+1])
            for i in range(n):
                result[i] = sum_window
                sum_window = sum_window-code[left]
                left = (left+1)%n
                right = (right+1)%n
                sum_window+=code[right]
        else:
            left = n-abs(k)
            right = n-1 
            sum_window = sum(code[left:right+1])
            for i in range(n):
                result[i]=sum_window
                sum_window=sum_window-code[left]
                left = (left+1)%n
                right = (right+1)%n
                sum_window+=code[right]
        
        return result
               
            

obj = Solution()
r=obj.decrypt(code = [2,4,9,3], k = -2)
print(r)