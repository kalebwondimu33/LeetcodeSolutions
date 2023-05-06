class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        if 0 in s:
            c = 1
        return (len(s) - c)
                
            
    
            
        
        
        
        