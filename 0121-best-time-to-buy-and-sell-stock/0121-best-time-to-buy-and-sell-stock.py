class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxdiff=0
        if len(prices)==1:
            return 0
        while right < len(prices):
            if prices[right]< prices[left]:
                left = right
                right+=1
                continue
            maxdiff=max(maxdiff,prices[right]-prices[left])
            right+=1
        return maxdiff