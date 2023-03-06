class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0
        right=1
        while left<right and right<len(prices):
            if prices[right]<prices[left]:
                left=right
                right+=1
            else:
                profit=max(profit,prices[right]-prices[left])
                right+=1
        return profit
            
                
             
                    
                
        