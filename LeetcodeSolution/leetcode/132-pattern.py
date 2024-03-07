class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        min_=nums[0]
        for v in nums[1:]:
            while stack and v>=stack[-1][0]:
                stack.pop()
            if stack and v>stack[-1][1]:
                return True
            stack.append([v,min_])
            min_=min(min_,v)
        return False

           