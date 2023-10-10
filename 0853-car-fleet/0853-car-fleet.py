class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Stack = []
        time = 0
       # position_speed = sorted(zip(position, speed), reverse=True)
        dicts={}
        for i in range(len(position)):
            dicts[position[i]]=speed[i]
        position.sort(reverse=True)
        for positions in position:
            time = (target - positions) / dicts[positions]
            
            if not Stack or time > Stack[-1]:
                Stack.append(time)
        
        return len(Stack)

    
    
    