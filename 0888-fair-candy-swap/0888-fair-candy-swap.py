class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a,b=sum(A),sum(B)
        diff=(a-b)//2
        i,j=0,0
        A.sort()
        B.sort()
        while i<len(A) and j<len(B):
            temp = A[i]-B[j]
            if temp == diff:
                return [A[i],B[j]]
            elif temp<diff:
                i+=1
            else:
                j+=1
        
        
        
        