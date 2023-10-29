class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        out=[]
        i=0
        while i<(len(s)-1):
            j=i
            while j<(len(s)-1) and s[j]==s[j+1]:
                j+=1
            if (j-i+1)>=3:
                out.append([i,j])
            i=j
            i+=1
        return out
        