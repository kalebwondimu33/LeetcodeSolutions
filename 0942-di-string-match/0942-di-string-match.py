class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer=[]
        dec=len(s)
        inc=0
        
        for i in range(len(s)):
            if s[i]=="I":
                answer.append(inc)
                inc+=1
            elif s[i]=="D":
                answer.append(dec)
                dec-=1
        if s[len(s)-1]=="I":
            answer.append(inc)
        else:
            answer.append(dec)
        return answer