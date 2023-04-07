class Solution:
    def minimumSum(self, num: int) -> int:
        num=str(num)
        result=[]
        for i in num:
            result.append(i)
        result.sort()
        first=result[0]
        second=result[1]
        third=result[2]
        four=result[3]
        return int(first+four)+int(second+third)
        
            
        
        
        
        
        