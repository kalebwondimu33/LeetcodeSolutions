class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shash={}
        thash={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            schar=s[i]
            tchar=t[i]
            if schar not in shash:
                shash[schar]=tchar
            if tchar not in thash:
                thash[tchar]=schar
            if shash[schar]!=tchar or thash[tchar]!=schar:
                return False
        return True
        