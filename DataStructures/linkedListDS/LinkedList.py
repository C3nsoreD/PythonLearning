
from linkedListDS.Node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None  # This is he beginning node the head of the list!!
        self.counter = 0

    #  o(n)
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data, end=' ')
            # print()
            actualNode = actualNode.nextNode
        print()

    #  o(1) Addding new items on the list is constant time complex!!
    def insertStart(self, data):

        self.counter += 1

        newNode = Node(data)

        if not self.head:  # if it is a null pointer ie empty then
            self.head = newNode  # sets it to a newNode which contains the data
        else:
            newNode.nextNode = self.head  # Makes the newNode the "head" BY pointing to the next node
            self.head = newNode  # Sets the "head" to the data

    #  o(1) insteda of O(N)

    def size(self):
        return self.counter

    #  O(N) adding new data at the end of the lis is linear time complex!!
    def insertEnd(self, data):

        newNode = Node(data)
        actualNode = self.head

        if self.head is None:  # checks if "head" is empty
            self.insertStart(data)
            return

        while actualNode.nextNode is not None: # Checks if its not null then  traverses through the list
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def remove(self, data):
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)