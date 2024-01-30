class Solution:
    def balancedString(self, s: str) -> int:
        k=len(s)//4
        count=Counter(s)
        left=0
        right=0
        maxx=max(count.values())
        res=float("inf")
        if maxx==k:
            return 0
        for right in range(len(s)):
            count[s[right]]-=1
            while left<len(s) and count['Q']<=k and count['W']<=k and count['E']<=k and count['R']<=k:
                count[s[left]]+=1
                res=min(res,right-left+1)
                left+=1
        return res
           

           
        
        return ans