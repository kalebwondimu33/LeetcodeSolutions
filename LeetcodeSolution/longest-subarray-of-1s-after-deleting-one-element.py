class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums))==1 and nums[0]==1:
            return len(nums)-1
        left=0
        dic={}
        zero=0
        maxx=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
                if zero>1:
                    left=dic[0]+1
                    zero-=1
                dic[nums[right]]=right
            if zero<1:
                maxx=max(maxx,right-left+1)
            if zero==1:
                maxx=max(maxx,right-left)
        return maxx


                



        