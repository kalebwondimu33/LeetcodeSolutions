class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        tb=[0,1]
        if n==0:
            return 0
        for i in range(1,n+1):
            if i*2<=n:
                tb.append(tb[i])
                # tb[2*i]=tb[i]
            if i*2+1<=n:
                tb.append(tb[i]+tb[i+1])
                # tb[i*2+1]=tb[i]+tb[i+1]
            else:
                break
        return max(tb)
            
        