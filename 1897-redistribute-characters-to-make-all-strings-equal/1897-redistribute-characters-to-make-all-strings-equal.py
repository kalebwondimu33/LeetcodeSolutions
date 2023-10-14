class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        join=''.join(words)
        set1=set(join)
        for i in set1:
            if join.count(i)%len(words)!=0:
                return False
        return True