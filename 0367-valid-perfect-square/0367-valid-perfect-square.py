class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i*i==num:
                return True
            elif i*i>num:
                return False
       
        