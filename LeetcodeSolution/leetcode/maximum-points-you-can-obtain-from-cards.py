class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        left,right=0,n-k
        total=sum(cardPoints[right:])
        res=total
        while right<n:
            total+=(cardPoints[left]-cardPoints[right])
            res=max(res,total)
            left+=1
            right+=1
        return res


        




