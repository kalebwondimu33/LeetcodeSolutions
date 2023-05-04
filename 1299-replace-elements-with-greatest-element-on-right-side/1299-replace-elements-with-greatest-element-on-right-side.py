class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reverse=arr[::-1]
        maximum=-1
        for i in range(len(reverse)):
            reverse[i],maximum=maximum,max(maximum,reverse[i])
        return reverse[::-1]
            
                
            
            
       
            
            
            
        
                
            
            
        