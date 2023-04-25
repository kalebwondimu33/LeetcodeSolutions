class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hashtable={'a':'white','b':'black','c':'white','d':'black','e':'white','f':'black','g':'white','h':'black'}
        first=coordinates[0]
        second=int(coordinates[1])
        if hashtable[first]=='white' and second%2==0:
            return True
        elif hashtable[first]=='black' and second%2==0:
            return False
        elif hashtable[first]=='white' and second%2!=0:
            return False
        else:
            return True
            
        