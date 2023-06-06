class Solution:
    def minimizedStringLength(self, s: str) -> int:
        stack=[]
        for i in s:
            if stack and i in stack:
                pass
            else:
                stack.append(i)
        return len(stack)
        