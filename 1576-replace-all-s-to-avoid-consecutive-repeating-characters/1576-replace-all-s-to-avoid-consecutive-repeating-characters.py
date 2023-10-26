class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==1 and s[0]=="?":
            return "a"
        ss=list(s)
        for i in range(len(ss)):
            if ss[i]=="?":
                for j in "abc":
                    if i==0 and ss[i+1]!=j:
                        ss[i]=j
                        break
                    elif i==len(ss)-1 and ss[i-1]!=j:
                        ss[i]=j
                        break
                    elif ss[i-1]!=j and ss[i+1]!=j:
                        ss[i]=j
                        break
        return ''.join(ss)
    
    


   