class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            elif nums[i] < nums[i - 1]:
                increasing = False
        
        return increasing or decreasing
