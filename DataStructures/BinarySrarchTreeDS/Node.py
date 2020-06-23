# BST Basic working principle: Root node is the first one at the top and a maximum of 2 nodes can be created
# Left node is always smaller than the root and right node is greater than the root


class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):
        if value < self.data:
            if not self.leftChild:
                self.leftChild = Node(value)
            else:
                self.leftChild.insert(value)
        else:
            if not self.rightChild:
                self.rightChild = Node(value)
            else:
                self.rightChild.insert(value)

    def remove(self, value, parentNode):
        if value < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(value, self)
        elif value > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(value, self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMin()
                self.rightChild.remove(self.data, self)
            elif parentNode.leftChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode = self.rightChild

            elif parentNode.righChild == self:
                if self.rightChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.rightChild = tempNode

    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()




