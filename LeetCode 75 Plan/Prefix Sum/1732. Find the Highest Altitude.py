class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # The biker always starts at altitude 0
        current_altitude = 0
        
        # Keep track of the maximum altitude reached, starting at the baseline 0
        highest_altitude = 0

        # Loop through each elevation change in the trip
        for change in gain:
            # Update the current altitude by adding the gain (or loss)
            current_altitude += change
            
            # If our new altitude is a record high, update our tracker
            if current_altitude > highest_altitude:
                highest_altitude = current_altitude
                
        # Return the highest point reached during the whole trip
        return highest_altitude
    
obj = Solution()
print(obj.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))