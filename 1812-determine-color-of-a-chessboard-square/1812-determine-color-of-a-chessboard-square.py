class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hashtable={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
        first=coordinates[0]
        second=int(coordinates[1])
        if (hashtable[first]+second)%2==0:
            return False
        else:
            return True
            
        