class Solution:
    def reformat(self, s: str) -> str:
        digit=[]
        alpha=[]
        ans=""
        for i in s:
            if i.isdigit():
                digit.append(i)
            elif i.isalpha():
                alpha.append(i)
        if abs(len(digit)-len(alpha))>1:
            return ''    
        if len(alpha)>len(digit):
            for i in range(len(digit)):
                ans+=alpha[i]
                ans+=digit[i]
            ans+=alpha[-1]
        elif len(alpha)<len(digit):
            for j in range(len(alpha)):
                ans+=digit[j]
                ans+=alpha[j]
            ans+=digit[-1]
        else:
            for k in range(len(alpha)):
                ans+=alpha[k]
                ans+=digit[k]
        return ans
                
                