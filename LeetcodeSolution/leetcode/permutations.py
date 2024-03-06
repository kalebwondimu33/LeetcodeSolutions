class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation=[]
        def recursive(nums,i):
            if i==len(nums)-1:
                permutation.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                recursive(nums,i+1)
                nums[i],nums[j]=nums[j],nums[i]
        recursive(nums,0)
        return permutation
        