class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 从终点往前，因为离终点越远的越可能已经碰撞了
        #closest to target first)
        pair = [(p,s) for p, s in zip(position,speed)]
        pair.sort(reverse ="True")
        # list of tuple
        prevTime = (target-pair[0][0])/pair[0][1]
        fleets = 1
        for i in range(len(pair)):
            curcar = pair[i]
            curTime = (target - pair[i][0])/pair[i][1]
            if curTime > prevTime:
                fleets += 1
                prevTime = curTime
        return  fleets




        