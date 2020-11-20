class Bag:
    def __init__(self):
        self._theitems = list()

    # Returns the number of items
    def __len__(self):
        return len(self._theitems)

    # Determines if an item is contained in the bag
    def __contains__(self, item):
        return item in self._theitems

    # Adds an item in the bag
    def add(self, item):
        return self._theitems.append(item)

    # Specially removes an item
    def remove(self, item):
        # Precondition to check if the index exists
        assert item in self._theitems, "The item must be in the bag"
        ndx = self._theitems.index(item)
        return self._theitems.pop(ndx)

    # Defines an iterator for traversing the list of items
    def __iter__(self):
        return _BagIterator(self._theitems)


class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0  # The _curItem is an indexing variable

    def __iter__(self):
        return self

    # THIS IS A LOOP METHOD
    # Called to return the next item in the container
    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
