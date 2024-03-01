class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        while n>1:
            reminder=n%3
            if reminder!=0:
                return False
            else:
                n=n/3
        return True
            
        
        