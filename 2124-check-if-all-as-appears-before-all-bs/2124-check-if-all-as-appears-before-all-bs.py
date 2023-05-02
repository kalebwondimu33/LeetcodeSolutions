class Solution:
    def checkString(self, s: str) -> bool:
        stack=[]
        for i in s:
            if stack and stack[-1]=="b" and i=="a":
                return False
            else:
                stack.append(i)
        return True
                
            