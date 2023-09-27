class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        num=[]
        for i in range(1,n):
            if '0' not in str(i):
                num.append(i)
        left=0
        right=len(num)-1
        while left<=right :
            if num[left]+num[right]==n:
                return [num[left],num[right]]
            elif num[left]+num[right]>n:
                right-=1
            else:
                left+=1
        
        