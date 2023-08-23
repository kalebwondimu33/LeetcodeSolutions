class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        per=[]
        res=[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def dfs():
            if len(per)==len(nums):
                res.append(per.copy())
                return
            for n in count:
                if count[n]>0:
                    per.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    per.pop()
        dfs()
        return res
        