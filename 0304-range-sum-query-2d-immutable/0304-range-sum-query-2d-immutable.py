class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,columns=len(matrix),len(matrix[0])
        self.newmat=[[0]*(columns+1) for r in range(rows+1) ]

        for r in range(rows):
            prefix=0
            for c in range(columns):
                prefix += matrix[r][c]
                above =self.newmat[r][c+1]
                self.newmat[r+1][c+1]=prefix +above
               

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1

        bottom_right=self.newmat[row2][col2]
        above=self.newmat[row1-1][col2]
        left=self.newmat[row2][col1-1]
        top_left=self.newmat[row1-1][col1-1]
        return bottom_right -above-left+top_left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)