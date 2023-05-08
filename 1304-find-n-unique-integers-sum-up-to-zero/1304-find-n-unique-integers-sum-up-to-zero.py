class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [ int(i * 2 - n + 1) for i in range(n)]
        return result
            
        