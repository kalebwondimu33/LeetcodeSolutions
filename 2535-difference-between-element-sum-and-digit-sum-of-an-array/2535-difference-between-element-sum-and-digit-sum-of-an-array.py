class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=sum(nums)
        ss=""
        for i in nums:
            ss+=str(i)
        digit_sum=0
        for i in ss:
            digit_sum+=int(i)
        return abs(element_sum-digit_sum)
        