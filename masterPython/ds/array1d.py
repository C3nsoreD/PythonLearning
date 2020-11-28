"""
Creating a simple word counter, 
using ASCII code to count the number of letters 
"""
import ctypes


class Array:
    def __init__(self, size):
        assert size > 0, 'Size must be > 0'
        self._size = size
        # Create a c type py object
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Inializes the array with None
        self.clear(None)
    
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        # check if the index is legal
        # using asserts is more informative and pythonic
        assert index >= 0 and index < len(self), 'Index is out of bounds'
        return self._elements[index]        

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'Index not in bounds, check array size'
        self._elements[index] = value
    
    # define an iterator
    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        return self._elements

class _ArrayIterator:
    def __init__(self, ArrayType):
        self._array_ref = ArrayType
        self._cur_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration

