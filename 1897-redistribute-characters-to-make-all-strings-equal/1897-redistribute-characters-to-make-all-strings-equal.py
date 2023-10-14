class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        join=''.join(words)
        set1=set(join)
        dic=Counter(join)
        for i in set1:
            if dic[i]%len(words)!=0:
                return False
        return True