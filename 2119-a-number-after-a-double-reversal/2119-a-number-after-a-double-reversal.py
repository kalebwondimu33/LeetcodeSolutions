class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        nums=str(num)
        num1=int(nums[::-1])
        num2=str(num1)[::-1]
        if int(num2)==num:
            return True
        else:
            return False
        
        