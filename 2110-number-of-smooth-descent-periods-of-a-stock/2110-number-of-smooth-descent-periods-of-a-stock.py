class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[1]*n
        for i in range(1,n):
            if prices[i]==prices[i-1]-1:
                dp[i]=dp[i-1]+1
        return sum(dp)
        