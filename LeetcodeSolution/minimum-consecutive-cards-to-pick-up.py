class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        ans=float("inf")
        for r in range(len(cards)):
            if cards[r] not in dic:
                dic[cards[r]]=r
            else:
                ans=min(ans,r-dic[cards[r]]+1)
                dic[cards[r]]=r
        if ans==float("inf"):
            return -1
        else:
            return ans
            

        