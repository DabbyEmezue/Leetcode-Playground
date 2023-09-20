class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for index,value in enumerate(nums):
            if index>0 and value == nums[index-1]:
                continue
            left=index+1
            right=len(nums)-1
            while left<right:
                sum = value + nums[left] + nums[right]
                if sum < 0:
                    left+=1
                    continue
                elif sum>0:
                    right-=1
                    continue
                else:
                    ans.append([value,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        return ans