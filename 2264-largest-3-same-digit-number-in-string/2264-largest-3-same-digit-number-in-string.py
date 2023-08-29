class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m,l=[],["000","111","222","333","444","555","666","777","888","999"]
        for i in l:
            if i in num:
                m.append(i)
        m.sort()
        return m[-1] if len(m)>0 else ""
        