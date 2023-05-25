class Solution:
    def reverse(self, x: int) -> int:
        xx=str(x)
        if xx[0]=="-":
            if -int(xx[1:][::-1])<(-2**31):
                return 0
            else:
                return -int(xx[1:][::-1])
        else:
            if int(xx[0:][::-1])>(2**31-1):
                return 0
            else:
                 return int(xx[0:][::-1])
        