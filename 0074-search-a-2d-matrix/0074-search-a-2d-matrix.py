class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        last=len(matrix[0])
        bottom=len(matrix)-1
        while top<=bottom:
            mid=(top+bottom)//2
            if matrix[mid][0]>target:
                bottom=mid-1
            elif matrix[mid][last-1]<target:
                top=mid+1
            else:
                break
        if top>bottom:
            return False
        l=0
        r=last-1
        while l<=r:
            m=(r+l)//2
            if matrix[mid][m]==target:
                return True
            elif matrix[mid][m]<target:
                l=m+1
            else:
                r=m-1
        return False
                
        