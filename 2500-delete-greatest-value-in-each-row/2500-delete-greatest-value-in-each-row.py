class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sorted_grid=[sorted(row) for row in grid]
        combine=list(zip(*sorted_grid))
        ans=0
        for i in range(len(combine)):
            ans+=max(combine[i])
        return ans
                

    
        