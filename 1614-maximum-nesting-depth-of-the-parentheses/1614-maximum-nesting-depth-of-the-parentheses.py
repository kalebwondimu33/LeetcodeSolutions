class Solution:
    def maxDepth(self, s: str) -> int:
        stack,mx=[],0
        for i in s:
            if i=="(":
                stack.append(i)
                mx=max(mx,len(stack))
            elif i==")":
                stack.pop()
        return mx
       
            
        