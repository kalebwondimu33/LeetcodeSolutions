class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxx=0
        for i in range(1,len(points)):
           maxx=max(maxx,points[i][0]-points[i-1][0]) 
        return maxx

        