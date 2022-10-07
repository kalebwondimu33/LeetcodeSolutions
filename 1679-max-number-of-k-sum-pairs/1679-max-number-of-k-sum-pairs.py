class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result=0
        d={}
        for x in nums:
            t=k-x
            if t in d and d[t]>0:
                result+=1
                d[t]-=1
            else:
                if x not in d:
                    d[x]=0
                d[x]+=1
        return result
       
                
                
                
            
        