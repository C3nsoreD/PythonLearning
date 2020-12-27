class Progression:
    """ Iterator producing a generic progression """

    def __init__(self, start=0):
        self._current = start   # Initialize the current value to start

    def _advance(self):
        """ Update self._current to a new value """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration Error """
        if self._current is None:   # our convention to end a proogression
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention an iter must return itself as an iterator """
        return self
    
    def print_progression(self):
        """ Print next n value of the progression """
        print(''.join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):
    """Creates an arithemtic progression """

    def __init__(self, increment=1, start=0):
        """ Create a new arithmetic progression:
            increment: the constant to add to each term 
            start: the starting point of each progresson """ 
        super().__init__(start)
        self._increment = increment
    