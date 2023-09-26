class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n):
            digits =str(n)
            nd=len(digits)
            if nd%2 !=0:
                return False
            lh=digits[:nd//2]
            rh=digits[nd//2:]
            ls=sum(map(int,lh))
            rs=sum(map(int,rh))

            return ls==rs
        count=0
        for i in range(low,high+1):
            if is_symmetric(i):
                count +=1
        
        
        return count
   