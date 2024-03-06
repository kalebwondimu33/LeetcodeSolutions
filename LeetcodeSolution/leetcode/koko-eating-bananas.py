class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        best=len(piles)
        while left<=right:
            mid=(left+right)//2
            calculate_hour=0
            for i in range(len(piles)):
                calculate_hour+=ceil(piles[i]/mid)
            if calculate_hour>h:
                left=mid+1
            else:
                right=mid-1
                best=mid
        return best


        