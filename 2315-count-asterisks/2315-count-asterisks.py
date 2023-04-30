class Solution:
    def countAsterisks(self, s: str) -> int:
        ans,t = 0,0
        for i in s:
            if i=="|":
                t+=1
            elif t%2==0:
                if i=="*":
                    ans+=1
        return ans
            
            
                