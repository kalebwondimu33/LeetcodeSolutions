class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        N=len(arr)
        n=0
        output=0
        for k,v in sorted(c.items(),key=lambda x:-x[1]):
            n+=v
            output+=1
            if n>=(N//2):
                break
        return output
           
        
            
            
        
        