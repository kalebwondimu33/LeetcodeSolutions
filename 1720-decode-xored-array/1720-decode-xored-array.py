class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        count=first
        for i in encoded:
            value=count^i
            count=value
            result.append(value)
        return result
        
            
        
        