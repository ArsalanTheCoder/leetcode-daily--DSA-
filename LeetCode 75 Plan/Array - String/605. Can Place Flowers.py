class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Fix 1: Handle edge case where n is already 0
        if n == 0:
            return True

        # Fix 2: Add padding so your loop covers the first and last real spots
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        # Loop runs from index 1 to len-1 (which now covers all REAL plots)
        for i in range(1, len(flowerbed)-1):
            
            # Check logic (Same as yours)
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  # Fix 3: Use assignment (=), NOT insert!
                n -= 1
                
                if n == 0:
                    return True
        
        return False

obj = Solution()
print(obj.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))