class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        best=max(nums)
        while left<=right:
            mid=(left+right)//2
            count=0
            kk=1
            for i in range(len(nums)):
                count+=nums[i]
                if count>mid:
                    count=nums[i]
                    kk+=1
            if kk>k:
                left=mid+1
            else:
                best=mid
                right=mid-1
        return best

