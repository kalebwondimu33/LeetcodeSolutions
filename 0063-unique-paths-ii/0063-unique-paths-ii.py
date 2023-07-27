class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        row=[0]*n
        row[n-1]=1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if grid[i][j]:
                    row[j]=0
                elif j+1<n:
                    row[j]=row[j]+row[j+1]
        return row[0]
                
        
        
                    
        