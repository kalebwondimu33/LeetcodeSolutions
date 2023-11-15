class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        maxx=0
        idx=0
        for i,v in enumerate(words):
            if len(v)>maxx:
                maxx=len(v)
                idx=i
        ans=[]
        j=0
        while j<maxx:
            temp=""
            for i,k in enumerate(words):
                if j<len(k):
                    temp+=k[j]
                else:
                    temp+=" "
            
            ans.append(temp.rstrip())
            j+=1
        return ans
                
                
        
        
        