class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        
        # Step 1: Start with Infinity as min_diff so the first pair always beats it
        min_diff = float('inf')
        result = []
        
        for i in range(len(arr) - 1):
            curr_diff = arr[i+1] - arr[i]
            
            # Case 1: Agar humein NAYA sabse chota difference mila
            if curr_diff < min_diff:
                min_diff = curr_diff   # Min diff update karo
                result = []            # Purani list phenk do (Reset)
                result.append([arr[i], arr[i+1]]) # Naya pair dalo
            
            # Case 2: Agar ye difference current min ke barabar hai
            elif curr_diff == min_diff:
                result.append([arr[i], arr[i+1]]) # Bas add kardo
                
        return result

# Test
obj = Solution()
print(obj.minimumAbsDifference([1, 5, 6])) 
# Output: [[5, 6]] (Correct!)