class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        for idx,i in enumerate(s):
            if not stack:
                stack.append(i)
            elif i in stack:
                continue
            else:
                while stack and (i < stack[-1]):
                    if stack[-1] in s[idx+1:]:
                        stack.pop()
                    else:
                        break
                stack.append(i)
        return ''.join(stack)
        
        
                
        
        