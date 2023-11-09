class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        signature = set()
        
        # Use pair of sorted even substring and odd substring as unique key
        
        for idx, s in enumerate(A):
            signature.add( ''.join( sorted( s[::2] ) ) + ''.join( sorted( s[1::2] ) )  )
        
        return len( signature )
        