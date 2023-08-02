class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        left=0
        right=1
        prices.sort()
        while left<right and right<len(prices):
            if prices[left]+prices[right]<=money:
                return money-(prices[left]+prices[right]) 
            else:
                return money
        