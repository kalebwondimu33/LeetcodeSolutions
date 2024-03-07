class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        mod=10**9+7
        right=len(nums)-1
        for left in range(len(nums)):
            print(left,right)
            while nums[left]+nums[right]>target and left<=right :
                right-=1
            if left<=right:       
                ans+=(2**(right-left))
        return ans%mod


        