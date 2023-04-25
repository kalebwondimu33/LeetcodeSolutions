class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashtable={}
        for i in s:
            if i in hashtable:
                return i
            hashtable[i]=1
        