class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r=len(height)-1
        while l!=r:
            b=r-l
            area = min(height[l],height[r])*b
            ans=max(ans,area)
            
            if height[l]>height[r]:
                r-=1
            elif height[r]>height[l]:
                l+=1
            else:
                r-=1
        return ans