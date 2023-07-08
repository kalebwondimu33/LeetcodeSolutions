class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        maxx=max(nums)
        minn=min(nums)
        for i in nums:
            if i !=maxx and i!=minn:
                return i
        