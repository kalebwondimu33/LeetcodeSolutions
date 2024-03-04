class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1]*len(nums)
        for index,value in enumerate(nums):
            while stack and stack[-1][0]<value:
                result[stack[-1][1]]=value
                stack.pop()
            stack.append((value,index))
        for index,value in enumerate(nums):
            while stack and stack[-1][0]<value:
                result[stack[-1][1]]=value
                stack.pop()
        return result
        
            
        
        