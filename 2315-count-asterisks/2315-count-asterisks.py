class Solution:
    def countAsterisks(self, s: str) -> int:
        p,r=False,0
        for i in s:
            if i=="*" and not p:
                r+=1
            elif i=="|":
                p=not p
        return r
                