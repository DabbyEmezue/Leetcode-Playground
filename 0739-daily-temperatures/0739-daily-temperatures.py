class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Stack=[]
        ans = [0] *len(temperatures)
        for i in range(len(temperatures)):
            if len(Stack)==0:
                Stack.append(i)
                continue
            while Stack and temperatures[i]>temperatures[Stack[-1]] :
                j=Stack.pop()
                ans[j]=i-j
            Stack.append(i)
        return ans