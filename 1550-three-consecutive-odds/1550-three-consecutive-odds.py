class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        stack=[]
        for i in arr:
            if len(stack)>=2:
                if stack[-1]%2!=0 and stack[-2]%2!=0 and i%2!=0:
                    return True
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return False
                
            
        