class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        left=0
        right=1
        while left<right and right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right+=1
            else:
                diff=prices[right]-prices[left]
                profit=max(diff,profit)
                right+=1
        return profit
                
             
                    
                
        