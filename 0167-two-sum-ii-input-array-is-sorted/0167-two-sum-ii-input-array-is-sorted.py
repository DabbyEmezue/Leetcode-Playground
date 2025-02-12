class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while True:
            if numbers[left] + numbers[right] > target:
                right-=1
                continue
            if numbers[left] + numbers[right] < target:
                left+=1
                continue
            else:
                return [left+1,right+1]