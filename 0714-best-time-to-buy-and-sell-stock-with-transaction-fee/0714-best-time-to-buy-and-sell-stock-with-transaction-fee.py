class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit=0
        effectiveBuy=prices[0]
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-effectiveBuy-fee)
            effectiveBuy=min(effectiveBuy,prices[i]-profit)
        return profit
        