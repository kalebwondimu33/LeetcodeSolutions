class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for index,value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                stackvalue,stack_ind=stack.pop()
                result[stack_ind]=(index-stack_ind)
            stack.append([value,index])
        return result
        