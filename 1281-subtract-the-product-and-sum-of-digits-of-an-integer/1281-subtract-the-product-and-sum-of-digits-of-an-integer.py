class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        r=str(n)
        pro=1
        l=len(r)
        s=0
        res=[]
        for i in range(l):
            res.append(r[i])
            
        for i in res:
            pro*=int(i)
        for i in res:
            s+=int(i)
        return pro-s
        
        
        