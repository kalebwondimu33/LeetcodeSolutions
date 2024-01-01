class Solution:
    def findTheWinner(self, n: int, k: int) -> int:        
        game=[i for i in range(1,n+1)]
        current=len(game)-1
        while len(game)>1:
            current=(current+k)%len(game)
            game.remove(game[current])
            current-=1
            current%=len(game)
        return game[0]
        
            
       
        