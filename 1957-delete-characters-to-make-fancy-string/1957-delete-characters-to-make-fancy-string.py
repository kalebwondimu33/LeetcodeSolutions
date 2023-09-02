class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        for i in s:
            if not stack:
                stack.append(i)
            elif stack[-1]==i and len(stack)<2 :
                stack.append(i)
            elif stack[-1]==i and len(stack)>=2 and stack[-2]==i:
                pass
            else:
                stack.append(i)
        return ''.join(stack)
                
        