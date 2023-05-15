class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        small=min(nums)
        large=max(nums)
        for i in nums:
            if i>small and i<large:
                count+=1
        return count