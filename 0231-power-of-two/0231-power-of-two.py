class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        while n>1:
            remender=n%2
            if remender!=0:
                return False
            else:
                n=n/2
        return True
        