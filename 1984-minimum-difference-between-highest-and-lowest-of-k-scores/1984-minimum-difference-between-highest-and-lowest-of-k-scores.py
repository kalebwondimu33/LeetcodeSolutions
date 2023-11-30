class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j=0,k-1
        n=len(nums)
        m=float("inf")
        while j<n:
            m=min(m,nums[j]-nums[i])
            i+=1
            j+=1
        return m
            
            
                    
        
        
        
        