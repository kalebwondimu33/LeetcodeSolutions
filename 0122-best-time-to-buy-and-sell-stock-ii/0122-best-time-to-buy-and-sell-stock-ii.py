class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profite=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profite+=(prices[i]-prices[i-1])
        return profite
        