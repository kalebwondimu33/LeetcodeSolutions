class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                temp=j
                if prices[i]>=prices[j]:
                    output.append(prices[i]-prices[j])
                    break
            if prices[i]<prices[temp] or i==len(prices)-1:
                output.append(prices[i])
            
        return output
        