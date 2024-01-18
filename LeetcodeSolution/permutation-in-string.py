class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d=Counter(s1)
        k=len(s1)
        window_d=Counter(s2[:k])
        if s1_d==window_d:
            return True
        l=0
        r=k
        while l<r and r<len(s2):
            window_d[s2[l]]-=1
            if window_d[s2[l]]==0:
                window_d.pop(s2[l])
            if s2[r] in window_d:
                window_d[s2[r]]+=1
            elif s2[r] not in window_d:
                window_d[s2[r]]=1
            if window_d==s1_d:
                return True
            l+=1
            r+=1
        return False
        


        