class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix[0])):
                if j-1<0:
                    matrix[i][j]=min(matrix[i][j]+matrix[i+1][j],matrix[i][j]+matrix[i+1][j+1])
                elif j+1>=len(matrix[0]):
                    matrix[i][j]=min(matrix[i][j]+matrix[i+1][j],matrix[i][j]+matrix[i+1][j-1])
                else:
                    matrix[i][j]=min(matrix[i][j]+matrix[i+1][j],matrix[i][j]+matrix[i+1][j-1],matrix[i][j]+matrix[i+1][j+1])
        return min(matrix[0])
                    
                    
            
        
        