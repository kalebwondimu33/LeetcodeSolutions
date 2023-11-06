class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>=len(part) and ''.join(stack[-len(part):])==part:
                for i in range(len(part)):
                    stack.pop()
                
        return ''.join(stack)
        