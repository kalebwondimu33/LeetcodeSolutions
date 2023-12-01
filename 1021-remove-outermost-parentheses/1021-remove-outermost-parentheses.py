class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
                if len(stack)>1:
                    res+=i
            else:
                stack.pop()
                if len(stack)>0:
                    res+=i
        return res
        
        