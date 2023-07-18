class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]*i for i in range(1,numRows+1)]
        for i in range(len(result)):
            left=0
            right=1
            if len(result[i])>2:
                j=1
                while j<len(result[i])-1:
                    result[i][j]=result[i-1][left]+result[i-1][right]
                    left+=1
                    right+=1
                    j+=1
        return result
                
                
                
                
            
            # [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
        