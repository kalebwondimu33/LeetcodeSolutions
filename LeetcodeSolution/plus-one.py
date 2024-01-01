class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        result_str="".join(str(i)for i in digits)
        result_int=str(int(result_str)+1)
        for i in range(len(result_int)):
            result.append(int(result_int[i]))
        return result
        
        
        
        