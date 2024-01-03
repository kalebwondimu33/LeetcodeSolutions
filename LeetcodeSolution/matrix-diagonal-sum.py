class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count1=len(mat)-1
        count2=0
        sum1=0
        sum2=0
        for i in mat:
            sum1+=i[count1]
            sum2+=i[count2]
            if count1==count2:
                sum1-=i[count1]
            count1-=1
            count2+=1
        return sum1+sum2
            
        