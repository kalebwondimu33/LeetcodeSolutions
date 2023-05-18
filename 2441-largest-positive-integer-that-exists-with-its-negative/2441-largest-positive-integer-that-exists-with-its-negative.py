class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            if -1*(nums[left])==nums[right]:
                return nums[right]
            elif -1*(nums[left])<nums[right]:
                right-=1
            else:
                left+=1
        return -1
        