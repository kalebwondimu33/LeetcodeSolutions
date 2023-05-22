class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        result=[]
        large=target[-1]
        for i in range(1,n+1):
            stack.append(i)
            result.append("Push")
            if i==large:
                return result
            if stack[-1] not in target:
                stack.pop()
                result.append("Pop")
        return result
        