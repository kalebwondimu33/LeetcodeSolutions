class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        temp=0
        for i in range(n):
            temp=temp^(start+2*i)
        return temp
        