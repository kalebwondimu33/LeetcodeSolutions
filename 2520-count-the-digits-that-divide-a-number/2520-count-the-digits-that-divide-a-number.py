class Solution:
    def countDigits(self, num: int) -> int:
        res=str(num)
        count=0
        for i in range(len(res)):
            if num%int(res[i])==0:
                count+=1
        return count
            
        