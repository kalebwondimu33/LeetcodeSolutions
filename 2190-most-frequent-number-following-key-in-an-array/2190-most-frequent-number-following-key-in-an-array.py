class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        dic={}
        maxx=0
        value=0
        for i in range(1,len(nums)):
            if nums[i-1]==key:
                if dic and  nums[i] in dic:
                    dic[nums[i]]+=1
                    if maxx<dic[nums[i]]:
                        maxx=dic[nums[i]]
                        value=nums[i]
                else:
                    dic[nums[i]]=1
                    if maxx<dic[nums[i]]:
                        maxx=dic[nums[i]]
                        value=nums[i]
        return value
        