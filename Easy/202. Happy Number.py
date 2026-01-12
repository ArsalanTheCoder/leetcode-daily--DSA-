class Solution(object):
    def happyNumber(self, no):
        seen = set()
        while True:
            sum = 0
            while no >0:
                digit = no%10
                sum+=digit**2
                no = no//10
            no = sum
            if sum in seen:
                return False
            seen.add(sum)
            if sum ==  1:
                return True
        
obj = Solution()
print(obj.happyNumber(2))
            