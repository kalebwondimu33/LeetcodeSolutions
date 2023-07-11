class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        stack=[]
        for i in words:
            if  stack and i[::-1] in stack:
                count+=1
            else:
                stack.append(i)
        return count