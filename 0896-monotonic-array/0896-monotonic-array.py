class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1]-nums[0]<0:
            nums.reverse()
        for index in range(len(nums)-1):
            if not nums[index]<=nums[index+1]:
                return False
        return True