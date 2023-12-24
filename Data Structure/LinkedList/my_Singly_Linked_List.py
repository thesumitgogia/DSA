class Node:
    def __init__(self, data=None, next=None):
        # Node class for a linked list.
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # Initializes an empty linked list.
        self.head = None

    def insertAtBeginning(self, value):
        # Inserts a new node with the given value at the beginning of the linked list.
        node = Node(value, self.head)
        self.head = node

    def insertAtEnd(self, value):
        # Inserts a new node with the given value at the end of the linked list.
        if not self.head:
            # If the list is empty, add to the beginning instead of the end.
            self.insertAtBeginning(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)

    def insertAfterNode(self, node, value):
        # Inserts a new node with the given value after a specified node.
        if self.head.data == node:
            self.head.next = Node(value, self.head.next)
            return
        temp = self.head
        while temp.next:
            if temp.next.data == node:
                new_node = Node(value, temp.next)
                temp.next = new_node
                return

    def deleteNodeByPosition(self, position):
        # Deletes a node at the specified position in the linked list.
        if not self.head:
            print("Linked List is Empty!")
            return
        if position < 0 or position > self.getLength() - 1:
            print("Invalid Position!")
            return
        if position == 0:
            # Special case: Deleting the head node.
            self.head = self.head.next
            return
        temp = self.head
        count = 0
        while temp:
            if position - 1 == count:
                temp.next = temp.next.next
                return
            temp = temp.next
            count += 1

    def getAtPosition(self, position):
        # Retrieves the data value at the specified position in the linked list.
        if not self.head:
            print("Linked List is Empty!")
            return None
        temp = self.head
        count = 0
        while temp:
            if position == count:
                return temp.data
            temp = temp.next
            count += 1

    def getLength(self):
        # Returns the length of the linked list.
        if not self.head:
            print("List is Empty!")
            return 0
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count

    def reverseList(self):
        # Reverses the linked list and prints the reversed list.
        if not self.head:
            print("Linked List is Empty!")
            return
        if not self.head.next:
            # Special case: Single-node linked list.
            print(str(self.head.data) + ' --> None')
            return
        temp = self.head
        arr = []
        while temp:
            arr.append(str(temp.data) + ' -> ')
            temp = temp.next
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i], end='')
        print('None')

    def isEmpty(self):
        # Checks if the linked list is empty.
        return not self.head

    def clear(self):
        # Clears the linked list (makes it empty).
        self.head = None

    def print(self):
        # Prints the elements of the linked list.
        if not self.head:
            print("List is Empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def insertList(self, values):
        # Inserts a list of values at the end of the linked list.
        if self.isEmpty():
            return
        for value in values:
            self.insertAtEnd(value)
            
    def deleteNodeByKey(self, key):
        # Deletes the first occurrence of a node with the specified key.
        pass

    def searchByKey(self, key):
        # Searches for a node with the specified key and returns its reference.
        pass


ll = LinkedList()
ll.insertAtBeginning(50)
ll.insertAtBeginning(40)
ll.insertAtBeginning(30)
ll.insertAtBeginning(20)
ll.insertAtEnd(60)
# print(ll.head.next.next.next.next.data)
# ll.print()
# ll.print()
# ll.insertAfterNode(20, 10)
ll.print()
# print(ll.getAtPosition(2))
# print(ll.isEmpty())

# print(ll.getLength())
# ll.deleteNodeByPosition(2)
# ll.print()
# ll.clear()
# ll.print()
# ll.reverseList()

# list = [24, 45, 23, 76]
# ll.insertByList(list)
ll.print()


# Methods to add
# insertAtBeginning(value)
# insertAtEnd(value)
# insertAfterNode(node, value)

# Methods to delete
# deleteNodeByKey(key)
# deleteNodeByPosition(position)

# Search and Access Methods
# searchByKey(key)
# getAtPosition(position)
# getLength()

# Traversal and Display Methods
# printList()
# reverseList()

# Other Methods
# isEmpty()
# clear()
