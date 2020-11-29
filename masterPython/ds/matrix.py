from .array2d import Array2D

class Matrix(Array2D):
    def __init__(self, numRows, numCols):
        super().__init__(numRows, numCols)
        self.clear(0)
    
    # def transpose(self):
    #     n, m = self.numCols(), self.numRows()
    #     _temp = Matrix(n, m)
    #     for i in range(self.numRows()):
    #         _row = self._Grid[i]
    #         for j in range(self.numCols()):
    #             _temp[j] = _row[i]
    #     return _temp

    def __getitem__(self, n_idx):
        return self[]
    