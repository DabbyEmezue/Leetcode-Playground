class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Stack = []
        maxArea= 0
        for index,height in enumerate(heights):
            start=index
            while Stack and height < Stack[-1][1]:
                top=Stack.pop()
                maxArea=max(maxArea, top[1]*(index-top[0]))
                start = top[0]
            Stack.append([start,height])
            
        for element in Stack:
            maxArea = max(maxArea,element[1]*(len(heights)-element[0]))
        return maxArea