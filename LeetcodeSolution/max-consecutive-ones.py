class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx_one=0
        current_one=0
        for i in nums:
            if i==1:
                current_one+=1
            else:
                current_one=0
            maxx_one=max(maxx_one,current_one)
        return maxx_one