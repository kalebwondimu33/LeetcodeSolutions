class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        dy = y1 - y0
        dx = x1 - x0
        
        for i in range(len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]
            
            if dx*(y - y1) != dy*(x - x1):
                return False
        else:
            return True