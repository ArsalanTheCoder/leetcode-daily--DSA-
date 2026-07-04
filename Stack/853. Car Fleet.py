class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))

        fleet = 0  #counter that counts the how many fleet
        lastTime = 0

        for position, speed in reversed(cars):
            time = (target-position)/speed
            if time > lastTime:
                fleet+=1
                lastTime = time
        return fleet      

obj = Solution()
answer = obj.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
print(answer)
