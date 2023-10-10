class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Stack = []
        time = 0
        position_speed = sorted(zip(position, speed), reverse=True)
        
        for pos, spd in position_speed:
            time = (target - pos) / spd
            
            if not Stack or time > Stack[-1]:
                Stack.append(time)
        
        return len(Stack)
