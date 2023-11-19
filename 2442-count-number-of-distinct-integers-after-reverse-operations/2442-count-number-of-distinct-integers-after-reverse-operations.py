class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            temp=str(nums[i])[::-1]
            nums.append(int(temp))
        return len(set(nums))
        