class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest=0
        highest_diff=0
        answer=0
        for num in nums:
            answer=max(answer,highest_diff*num)
            highest_diff=max(highest_diff,highest-num)
            highest=max(highest,num)
        return answer
            
        