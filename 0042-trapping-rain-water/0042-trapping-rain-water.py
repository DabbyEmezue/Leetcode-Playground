class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[]
        maxright = [0] * len(height)
        z=0
        ans=0
        for i in range(len(height)):
            maxleft.append(z)
            z=max(z,height[i])
        z=0
        for i in range(len(height)-1,-1,-1):
            maxright[i]=z
            z=max(z,height[i])
        for i in range(len(height)):
            temp = min(maxleft[i],maxright[i])
            if temp - height[i] >0:
                ans+= temp - height[i]
        return ans