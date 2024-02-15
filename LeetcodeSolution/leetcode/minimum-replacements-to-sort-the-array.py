class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
       
        ans=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=nums[i+1]:

                continue
            num_element=ceil(nums[i]/nums[i+1])
            ans+=num_element-1
            nums[i]=nums[i]//num_element
        return ans
        

        