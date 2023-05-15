class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        left=0
        right=len(nums)-1
        temp=1
        while temp<right:
            if nums[temp]>nums[left] and nums[temp]<nums[right]:
                count+=1
                temp+=1
            else:
                temp+=1
        return count