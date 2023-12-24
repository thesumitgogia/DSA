class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class Node:
    def __init__(self, prev=None, data=None, next=None):
        # Node class for a doubly linked list.
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        # Initializes an empty doubly linked list.
        self.head = None

    def isEmpty(self):
        return not self.head

    def insertAtBeginning(self, value):
        node = Node(None, value, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insertAtEnd(self, value):
        if self.isEmpty():
            self.insertAtBeginning(value)

        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(temp, value, None)
        temp.next = node



    def insertAfterNode(self, node, value):
        """
        Inserts a new node with the given value after a specified node.
        """
        pass

    def deleteNodeByKey(self, key):
        """
        Deletes the first occurrence of a node with the specified key.
        """
        pass

    def deleteNodeByPosition(self, position):
        """
        Deletes the node at the specified position.
        """
        pass

    def searchByKey(self, key):
        """
        Searches for a node with the specified key and returns its reference.
        """
        pass

    def getAtPosition(self, position):
        """
        Gets the value of the node at the specified position.
        """
        pass

    def getLength(self):
        """
        Gets the length of the doubly linked list.
        """
        pass

    def printForward(self):
        if self.isEmpty():
            return
        temp = self.head
        items = ''
        while temp.next:
            items += str(temp.data) + ' --> '
            temp = temp.next
        print(items + 'None')
    def printBackward(self):
        if self.isEmpty():
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        data = ''
        while temp:
            data += str(temp.data) + ' --> '
            temp = temp.prev
        print(data, end='None')

    def reverseList(self):
        """
        Reverses the order of elements in the doubly linked list.
        """
        pass

    def clear(self):
        self.head = None


dll = DoublyLinkedList()

dll.insertAtBeginning(20)
dll.insertAtBeginning(30)
dll.insertAtBeginning(40)
dll.insertAtBeginning(50)
dll.insertAtEnd(10)

dll.printBackward()