class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        ans=[]
        for i in range(n):
            if s[i]==c:
                ans.append(i)
        result=[]
        j=0
        for i in range(n):
            if s[i]==c:
                result.append(0)
                j+=1
            elif i<ans[0]:
                result.append(ans[0]-i)
            elif i>ans[-1]:
                result.append(i-ans[-1])
            else:
                result.append(min((ans[j]-i),(i-ans[j-1])))
        return result
    
    
           