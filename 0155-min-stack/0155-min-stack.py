import math
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minArray=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minArray[-1] if self.minArray else val)
        self.minArray.append(val)
        return

    def pop(self) -> None:
        self.minArray.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return
    def getMin(self) -> int:
        if len(self.minArray)>0:
            return self.minArray[-1]
        else:
            return
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()