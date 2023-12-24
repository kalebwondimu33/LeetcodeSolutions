class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count=0
        temp=right-left+1
        for i in range(left,right+1):
            for x,y in ranges:
                if x<=i<=y:
                    count+=1
                    break
        if temp==count:
            return True
        else:
            return False
                