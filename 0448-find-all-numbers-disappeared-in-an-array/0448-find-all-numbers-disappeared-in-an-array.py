class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp=len(nums)
        result=[]
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in range(1,temp+1):
            if i not in dic:
                result.append(i)
        return result
            
            
        
        