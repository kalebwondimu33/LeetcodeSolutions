class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        Row,Col=len(matrix),len(matrix[0])
        self.new_matrix=[[0]*(Col+1) for i in range(Row+1)] 
        for r in range(Row):
            prefix=0
            for c in range(Col):
                prefix+=matrix[r][c]
                above=self.new_matrix[r][c+1]
                self.new_matrix[r+1][c+1]=prefix+above

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        bottom_right=self.new_matrix[r2][c2]
        left=self.new_matrix[r2][c1-1]
        above=self.new_matrix[r1-1][c2]
        top_left=self.new_matrix[r1-1][c1-1]
        return bottom_right-left-above+top_left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)