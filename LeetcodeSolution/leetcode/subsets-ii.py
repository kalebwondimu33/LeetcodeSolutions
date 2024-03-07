class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(start,path=[]):
            if path in ans:
                return 
            if path not in ans:
                ans.append(path[:])
                
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0)
        return ans
        