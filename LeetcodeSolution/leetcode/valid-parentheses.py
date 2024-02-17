class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={")":"(","}":"{","]":"["}
        for i in range(len(s)):
            if s[i] not in dic:
                stack.append(s[i])
            elif stack and s[i] in dic and stack[-1]==dic[s[i]]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        
        