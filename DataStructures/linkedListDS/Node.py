

# Node class is the container of both the data nad the pointer to the next item on the list!


class Node(object):
    def __init__(self, data):
        self.data = data   # As data
        self.nextNode = None  # As pointer

#  method to remove data and references
    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode  #sets previous node to the nextnode (updates the references)
            del self.data  # deletes the data
            del self.nextNode  # and the pointer
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)
