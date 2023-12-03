class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        m1, m2 = {}, {}
        for i in range(n):
            m1[A[i]] = i
            m2[B[i]] = i
        c = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(i + 1):
                if m1[A[j]] <= i and m2[A[j]] <= i:
                    cnt += 1
            c[i] = cnt
        return c
                
                
                
                
                
                
        