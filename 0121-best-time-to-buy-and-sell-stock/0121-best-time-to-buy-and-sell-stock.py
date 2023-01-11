class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        result=0
        diff=0
        while right<len(prices):
            if prices[right]<prices[left]:
                left=right
                right+=1
            else:
                diff=prices[right]-prices[left]
                right+=1
            result=max(result,diff)
        return result
             
                    
                
        