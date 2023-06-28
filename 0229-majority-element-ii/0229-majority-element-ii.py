class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        result=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        n=len(nums)
        temp=n/3
        for i in dic:
            if dic[i]>temp:
                result.append(i)
        return result
        
        