class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        result=[1]*2
        for i in range(1,len(nums)+1):
            if i in count and count[i]==2:
                result[0]=i
            elif i not in count:
                result[1]=i
        return result
                
            
        