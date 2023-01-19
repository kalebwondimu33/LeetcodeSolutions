class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        result=0
        for i in words:
            for j in i:
                if j in allowed:
                    count+=1
            if count==len(i):
                result+=1
            count=0
        return result