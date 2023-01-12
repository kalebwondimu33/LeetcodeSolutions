class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        game=sorted(x+1 for x in range(n))
        current=len(game)-1
        while len(game)>1:
            current=(current+k)%len(game)
            game.remove(game[current])
            current-=1
            current%=len(game)
        return game[0]
        
        