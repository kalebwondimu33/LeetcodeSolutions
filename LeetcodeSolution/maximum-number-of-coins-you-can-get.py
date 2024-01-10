class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        k=len(piles)-2
        r=len(piles)-1
        total=0
        while  l<k and l<r:
            total+=piles[k]
            l+=1
            k-=2
            r-=2
        return total

        