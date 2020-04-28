#Author: C3nsored 

class Vector:

    def __init__(self, dim):
        """Create a vector with dim dimensions"""
        self._coords = [0] * dim
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, data):
        self._coords[i] = data
    
    def __add__(self, other):
        """ Returns sum of 2 vectors"""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")

        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
    
    def __eq__(self, other):
        return self._coords == other.__coords
    
    def __ne__(self, other):
        return self._coords != other.__coords
    
    def __str__(self):
        """Return string representaion of a Vector"""
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == "__main__":
    v = Vector(5)   # construct five-dimensional <0, 0, 0, 0, 0>
    
    v[1] = 23       # <0, 23, 0, 0, 0> (based on use of setitem )
    v[-1] = 45      # <0, 23, 0, 0, 45> (also via setitem )
    print(v[4])     # print 45 (via getitem )
    
    u = v + v       # <0, 46, 0, 0, 90> (via add )
    print(u)        # print <0, 46, 0, 0, 90>
    
    total = 0
    for entry in v: # implicit iteration via len and getitem
        total += entry  