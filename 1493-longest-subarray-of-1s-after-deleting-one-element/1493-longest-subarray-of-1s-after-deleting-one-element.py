class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best=0
        left=0
        right=0
        N=len(nums)
        current=0
        while right<N:
            if nums[right]==0:
                current+=1
            while current>1:
                if nums[left]==0:
                    current-=1
                left+=1
            right+=1
            best=max(best,right-left-1)
        return best
        