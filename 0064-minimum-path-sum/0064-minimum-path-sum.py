class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if i+1<len(grid):
                    if j+1<len(grid[0]):
                        grid[i][j]=min(grid[i][j]+grid[i][j+1],grid[i][j]+grid[i+1][j])
                    elif j==len(grid[0])-1:
                        grid[i][j]+=grid[i+1][j]
                elif i==len(grid)-1:
                    if j+1<len(grid[0]):
                        grid[i][j]+=grid[i][j+1]
        return grid[0][0]
            
        