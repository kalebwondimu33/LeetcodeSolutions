class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        lenn=len(s)
        for i in range(lenn):
            if(s[i]=='('):
                st.append(i)
            elif (s[i]==")"):
                temp=s[st[-1]:i +1]
                s=s[:st[-1]]+temp[::-1] + \
                    s[i+1:]
                del st[-1]
        res=""
        for i in range(lenn):
            if (s[i]!=')' and s[i]!='('):
                res+=(s[i])
        return res
        
               
                
            
        