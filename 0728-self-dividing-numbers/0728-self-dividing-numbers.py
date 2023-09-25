class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            check=str(i)
            count=0
            if '0' in check:
                continue
            else:
                for j in range(len(check)):
                    if i%int(check[j])==0:
                        count+=1
                if count==len(check):
                    result.append(int(check))
        return result
                
                    
            
            
            
        