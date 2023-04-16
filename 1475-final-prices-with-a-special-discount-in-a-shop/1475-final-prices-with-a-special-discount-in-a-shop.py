class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                temp=j
                if prices[i]>=prices[j]:
                    prices[i]=prices[i]-prices[j]
                    break
            if prices[i]<prices[temp] or i==len(prices)-1:
                prices[i]=prices[i]
            
        return prices
        