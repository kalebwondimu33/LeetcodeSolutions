class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        row=self.getRow(rowIndex-1)
        curr_row=[1]
        for i in range(1,rowIndex):
            curr_row.append(row[i-1]+row[i])
        curr_row.append(1)
        return curr_row