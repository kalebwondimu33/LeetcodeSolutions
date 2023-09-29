class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic={}
        ans=[]
        for i in nums:
            temp=set(i)
            for j in temp:
                if j in dic:
                    dic[j]+=1
                else:
                    dic[j]=1
        for k in dic:
            if dic[k]==len(nums):
                ans.append(k)
        return sorted(ans)
            
        
        