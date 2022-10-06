class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        while n>1:
            reminder=n%4
            if reminder!=0:
                return False
            else:
                n=n/4
        return True
        