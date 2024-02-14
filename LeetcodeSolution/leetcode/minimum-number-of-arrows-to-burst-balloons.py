class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        total=1
        pre=points[0]
        for s,e in points[1:]:
            if s>pre[1]:
                total+=1
                pre=[s,e]
            else:
                pre[1]=min(pre[1],e)
        return total
            
            
            
            
                
            
            
        
        # [[1, 6], [2, 8], [7, 12], [10, 16]]