class Solution:
    def tribonacci(self, n: int) -> int:
        ss=[0,1,1]
        if n<=2:
            return ss[n]
        for i in range(3,n+1):
            ss.append(ss[i-1]+ss[i-2]+ss[i-3])
        return ss[n]
            