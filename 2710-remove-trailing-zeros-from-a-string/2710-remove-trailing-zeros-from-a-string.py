class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        right=len(num)-1
        while True:
            if int(num[right])==0:
                right-=1
            else:
                break
        return num[:right+1]
        