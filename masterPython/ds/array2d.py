from .array1d import Array

class Array2D:
    def __init__(self, numRows, numCols):
        # define the row as the array 
        self._Rows = Array(numRows)
        self._Cols = Array(numCols) 
        # Create the cols 
        for i in range(numRows):
            self._Rows[i] = Array(numCols) 
    
    def numRows(self):
        return len(self._Rows)
    
    def numCols(self):
        return len(self._Cols)
    
    def clear(self, value):
        for row in range(self.numRows()):
            self._Rows[row].clear(value)
    
    # n_idx is a tuple
    def __getitem__(self, n_idx):
        assert len(n_idx) == 2, 'Invalid indexing. ex (1, 2)'
        row, col = n_idx
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array indexes out of range"
        the1dArray = self._Rows[row]
        # return self._Rows[row][col]
        # print(type(the1dArray[col]))
        return the1dArray[col]

    def __setitem__(self, n_idx, value):
        assert len(n_idx) == 2, 'Invalid indexing. ex (1, 2)'
        row = n_idx[0]
        col = n_idx[1]
        assert row >= 0 and row < self.numRows() and col >=0 and col < self.numCols(), "Array indexes out of range"
        _1dArray = self._Rows[row]
        self._Rows[col] = value


