class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        ind={}
        for i,v in enumerate(s):
            ind[v]=i
        for i in count:
            if count[i]==1:
                return ind[i]
        return -1
               
        