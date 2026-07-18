class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLUMN = len(matrix), len(matrix[0])
        self.sumat = [[0] * (COLUMN + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLUMN):
                prefix += matrix[r][c]
                above = self.sumat[r][c + 1]
                self.sumat[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        topleft = self.sumat[row1 - 1][col1 - 1]
        bottomright = self.sumat[row2][col2]
        left = self.sumat[row2][col1 - 1]
        above = self.sumat[row1 - 1][col2]
        return bottomright - above - left + topleft