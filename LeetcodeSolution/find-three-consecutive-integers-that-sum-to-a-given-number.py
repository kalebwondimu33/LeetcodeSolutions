class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]
        
        if num%3!=0:
            return ans
        else:
            mid=num//3
            return [mid-1,mid,mid+1]