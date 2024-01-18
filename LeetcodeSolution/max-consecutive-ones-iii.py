class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxx=0
        for r,v in enumerate(nums):
            k-=(1-v)
            if k<0:
                k+=(1-nums[left])
                left+=1
            maxx=max(maxx,r-left+1)

        return maxx
            

        