class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashtable={}
        for i in s:
            hashtable[i]=hashtable.get(i,0)+1
        temp=hashtable[s[0]]
        for i in hashtable:
            if hashtable[i]!=temp:
                return False
        return True
        