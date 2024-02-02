class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        curSum=0
        perfixsums={0:1}
        for n in nums:
            curSum+=n
            diff=curSum-k
            result+=perfixsums.get(diff,0)
            perfixsums[curSum]=1+perfixsums.get(curSum,0)
        return result
                
        
            
        