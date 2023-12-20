class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d={}
        maxx=0
        ans=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d:
            if maxx<d[j]:
                ans=j
                maxx=d[j]
        return ans
        
        