class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i,v in enumerate(nums):
            if v in dic and abs(dic[v]-i)<=k:
                    return True
            dic[v]=i
        return False
                
       
        