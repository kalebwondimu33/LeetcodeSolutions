class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i,v in enumerate(s):
            if v=="(":
                stack.append(i)
            elif v==")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while stack and star:
            if stack[-1]>star[-1]:
                return False
            stack.pop()
            star.pop()
        return len(stack)==0
    
    
    
    
    
    
    
      