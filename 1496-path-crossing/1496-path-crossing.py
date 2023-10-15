class Solution:
    def isPathCrossing(self, path: str) -> bool:
        lines=[(0,0)]
        x,y=0,0
        for i in path:
            if i=="N":
                y+=1
            if i=="S":
                y-=1
            if i=="E":
                x+=1
            if i=="W":
                x-=1
            if (x,y) in lines:
                return True
            else:
                lines.append((x,y))
        return False
        