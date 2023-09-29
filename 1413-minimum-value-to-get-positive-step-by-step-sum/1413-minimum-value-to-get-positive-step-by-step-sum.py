class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        Sum=0
        Min=0
        for number in nums:
            Sum=Sum+number
            Min=min(Sum,Min)
        return 1-Min