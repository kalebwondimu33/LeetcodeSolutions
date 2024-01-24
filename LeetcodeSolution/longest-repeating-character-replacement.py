class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        maxf=0
        left=0
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            maxf=max(maxf,count[s[right]])
            if (right-left+1)-maxf>k:
                count[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res



            
        
       

        
        