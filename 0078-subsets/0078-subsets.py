class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[]
        def recursive(nums,i,subset):
            if i==len(nums):
                output.append(subset[:])
                return
            recursive(nums,i+1,subset)
            subset.append(nums[i])
            recursive(nums,i+1,subset)
            subset.pop()
        recursive(nums,0,[])
        return output
        