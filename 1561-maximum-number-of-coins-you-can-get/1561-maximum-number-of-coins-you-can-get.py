class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count=0
        length=len(piles)//3
        while length:
            piles.pop()
            count=count+piles[-1]
            piles.pop()
            length-=1
        return count
        