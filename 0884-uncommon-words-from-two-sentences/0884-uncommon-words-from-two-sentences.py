class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        first=s1.split()
        second=s2.split()
        result=[]
        for i in first:
            if i not in second and first.count(i)==1:
                result.append(i)
        for i in second:
            if i not in first and second.count(i)==1:
                result.append(i)
        return result
        
        