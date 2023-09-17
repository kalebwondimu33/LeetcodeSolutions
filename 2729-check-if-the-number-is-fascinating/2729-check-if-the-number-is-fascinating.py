class Solution:
    def isFascinating(self, n: int) -> bool:
        total=str(n)
        total+=str(2*n)
        total+=str(3*n)
        count=0
        dic=Counter(total)
        num=[1,2,3,4,5,6,7,8,9]
        for i in num:
            if dic[str(i)]==1:
                count+=1
        if count==9:
            return True
        else:
            return False
        