class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=[(n,v)for v,n in count.items()]
        large=max(res)
        return large[1]
        