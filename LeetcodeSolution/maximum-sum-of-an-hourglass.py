class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx=0
        for i in range(len(grid)-2):
            l=0
            r=3
            k=0
            while l<r and r<=len(grid[0]):
                total=0
                if len(grid[i][l:r])==3:
                    total+=sum(grid[i][l:r])
                    k+=1
                    for j in range(i+1,i+3):
                        if j==i+1:
                            total+=grid[j][k]
                        else:
                            total+=sum(grid[j][l:r])
                    print(total)
                l+=1
                r+=1
                maxx=max(total,maxx)
        return maxx









        