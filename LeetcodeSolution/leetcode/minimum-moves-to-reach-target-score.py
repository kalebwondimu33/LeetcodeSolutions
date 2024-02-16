class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        remain=0
        while maxDoubles and target!=1:
          remain+=target%2
          target=target//2
          maxDoubles-=1
          count+=1
        return target-1+remain+count
          

        