class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest=max(nums)
        flag=True
        for i in nums:
            if i*2>largest and i!=largest:
                flag=False
                return -1
        if flag:
            return nums.index(largest)
        