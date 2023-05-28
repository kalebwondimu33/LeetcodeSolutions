class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1=Counter(s)
        cnt2=Counter(t)
        sm=0
        for i,j in cnt2.items():
            if i in cnt1 and j>cnt1[i]:
                sm+=abs(j-cnt1[i])
            elif i not in cnt1:
                sm+=j
        print(cnt1)
        print(cnt2)
        return sm
                
                
                
        