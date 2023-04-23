class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum=0
        right_sum=0
        total=0
        for i in range(1,n+1):
            total+=i
        fixed=total
        for i in range(1,n+1):
            right_sum=total-i
            left_sum=fixed-total
            if right_sum==left_sum:
                return i
            total-=i
        return -1
                    
            
        