class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        profit=0
        while left<right and right<len(prices):
            if prices[left]>prices[right]:
                left=right
                right+=1
            else:
                profit=max(profit,prices[right]-prices[left])
                right+=1
        return profit
            
                
             
                    
                
        