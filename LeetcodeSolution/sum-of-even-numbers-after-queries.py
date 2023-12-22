class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        even_sum=0
        for i in nums:
            if i%2==0:
                even_sum+=i
        for i in range(len(queries)):
            if nums[queries[i][1]]%2==0 and queries[i][0]%2==0 :
                even_sum+=queries[i][0]
            elif nums[queries[i][1]]%2==0 and queries[i][0]%2!=0:
                even_sum-=nums[queries[i][1]]
            elif nums[queries[i][1]]%2!=0 and queries[i][0]%2!=0:
                even_sum+=nums[queries[i][1]]+queries[i][0]
            nums[queries[i][1]]+=queries[i][0]
            result.append(even_sum)
             
            
        return result
        