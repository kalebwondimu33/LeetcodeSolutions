class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref={0:1}
        Sum=0
        result=0
        for num in nums:
            Sum+=num
            rem=Sum%k
            result+=pref.get(rem,0)
            pref[rem]=1+pref.get(rem,0)
        return result
            

        