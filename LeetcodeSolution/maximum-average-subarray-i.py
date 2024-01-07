class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Sum = 0
        for i in range(k):
            Sum += nums[i]

        maxSum = Sum
        i = k
        j = 0
        while i < len(nums):
            Sum -= nums[j]
            Sum += nums[i]
            maxSum = max(maxSum, Sum)
            i += 1
            j += 1
        return maxSum/k
        