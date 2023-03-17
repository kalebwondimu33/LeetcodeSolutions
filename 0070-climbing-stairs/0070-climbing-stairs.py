class Solution:
    def climbStairs(self, n: int) -> int:
        pre,nex=1,1
        for i in range(n-1):
            temp=nex
            nex=pre+nex
            pre=temp
        return nex
            
        
        
        
        